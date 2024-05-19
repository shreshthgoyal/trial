# Cult Support Chatbot

This is a pilot project to provide support to cult users via a chatbot. This is a LLM RAG Chatbot based on custom knowledge base.

> Currently, only the "cult" and "gym" section faq answers are considered as the knowledge base.

## Install and Run
```
# In the project repository
$ python3 -m venv venv
$ source venv/bin/activate
$ python -m pip install -r requirements.txt
$ python src/retriever/create_retriever.py
$ python invoke.py
```

## Folder Structure

![Folder Structure](https://i.ibb.co/bHS7KyS/Screenshot-2024-05-17-at-1-41-52-PM.jpg)

## Configuration 


| Key  | Value Information | Required |
| ------------- | ------------- | ------------- |
| `GOOGLE_API_KEY`  | Required to make calls and connect to the GEMINI API, you can sign up for a client id [here](https://aistudio.google.com/app/apikey).  | **Yes** |
| `TAVILY_API_KEY`  | Required to make searches on the internet to run the agent, you can sign up for a client secret [here](https://app.tavily.com/sign-in).  | **Yes** (Not if using OpenAI)|
| `LLM_MODEL`  | The LLM model version that will be used across the codebase.  | **Yes** |
| `EMBEDDING_MODEL`  | The embedding model version that will be used across the codebase.  | **Yes** |


Some additional details if they are required.


## Use cases

```
#General Queries about Cult, Programs offered, Gym etc.
	-User will be provided the response based on our knowledge base.
 
#Specific Pricing Queries
	- User will be provided a redirect link based on the query.

#Specific Gym Queries
	- User will be provided a redirect link based on the query.
    
# For any question that is out-of-scope, a default answer will be provided.
```

## Workflow

![Workflow of the chatbot](https://i.ibb.co/6vCKFw6/image.png)
