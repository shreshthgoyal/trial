import requests
from bs4 import BeautifulSoup
import csv

def fetch_html_content(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve URL: {url} with status code: {response.status_code}")
        return None
    return BeautifulSoup(response.text, 'html.parser')

def extract_hrefs_and_titles(soup, base_url):
    hrefs_and_titles = []
    sections = soup.find_all('section', class_='article-list')
    if not sections:
        print("No sections found.")
    for section in sections[:50]:  # Adjusted indices to specific sections
        for a_tag in section.find_all('a', href=True):
            href = base_url + a_tag['href']
            title = a_tag.get('title', 'No title provided')
            hrefs_and_titles.append((href, title))
    if not hrefs_and_titles:
        print("No hrefs and titles found.")
    return hrefs_and_titles

def fetch_faq_data(hrefs_and_titles, base_url):
    faq_data = []
    read_more_links = []
    for href, title in hrefs_and_titles:
        soup = fetch_html_content(href)
        if soup:
            questions_and_divs = soup.find_all('div', class_='c-row custom-c-article-row c-article-row')
            for question_div in questions_and_divs:
                question = question_div.find('div', class_='ellipsis article-title').get_text(strip=True)
                answer_div = question_div.find('div', class_='custom-text-color description-text')
                link = answer_div.a
                if link:
                    read_more_links.append((base_url + link['href'], title, question))
                else:
                    text = answer_div.get_text(strip=True)
                    if text:
                        faq_data.append((question, text, title))
    if not faq_data:
        print("No FAQ data found.")
    return faq_data, read_more_links

def fetch_additional_answers(read_more_links):
    additional_answers = []
    for link, title, question in read_more_links:
        soup = fetch_html_content(link)
        if soup:
            article_text = soup.find('article', class_='custom-article-body article-body').get_text(separator="\n", strip=True)
            additional_answers.append((question, article_text, title))
    return additional_answers

def clean_text(text):
    return text.replace('\xa0', ' ').replace('\n', ' ').strip()

def write_to_csv(filename, data):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Question', 'Answer', 'Title'])
        for question, answer, title in data:
            csv_writer.writerow([clean_text(question), clean_text(answer), title])

base_url = 'https://support.cult.fit'
soup = fetch_html_content(f'{base_url}/support/solutions')
if soup:
    hrefs_and_titles = extract_hrefs_and_titles(soup, base_url)
    faq_data, read_more_links = fetch_faq_data(hrefs_and_titles, base_url)
    faq_data.extend(fetch_additional_answers(read_more_links))
    csv_filename = 'data/faq_answers.csv'
    write_to_csv(csv_filename, faq_data)
    print(f"CSV file '{csv_filename}' created successfully with {len(faq_data)} entries.")
else:
    print("Failed to fetch the base URL content.")
