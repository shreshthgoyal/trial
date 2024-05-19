import dotenv
import os
from langchain_community.document_loaders import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from InstructorEmbedding import INSTRUCTOR


class CreateRetriever:
    def __init__(self):
        self.ANSWERS_CSV_PATH = "data/faq_answers.csv"
        self.ANSWERS_CHROMA_PATH = "chroma_data/"

        dotenv.load_dotenv()

        self.loader = CSVLoader(file_path=self.ANSWERS_CSV_PATH, source_column="Answer")
        self.answers = self.loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        texts = text_splitter.split_documents(self.answers)

        embeddings= GoogleGenerativeAIEmbeddings(model=os.getenv("EMBEDDING_MODEL"))

        self.answers_vector_db = Chroma.from_documents(texts, embeddings, persist_directory=self.ANSWERS_CHROMA_PATH)
    
    def get_retriever(self):
        return self.answers_vector_db.as_retriever(k=10)

answers_retriever = CreateRetriever().get_retriever()