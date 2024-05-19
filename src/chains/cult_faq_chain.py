import os
import dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import (
    PromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from src.retriever.create_retriever import answers_retriever

class CultFAQChain:
    def __init__(self):
        dotenv.load_dotenv()
        self.chat_model = GoogleGenerativeAI(model=os.getenv("LLM_MODEL"))

        cult_template_str = """
        Utilize the provided context to resolve the user's input. Ensure all answers are detailed, concise, and based on the provided context without adding any unverified information. 

        Guidelines:
        Context Usage: Base all responses on the given context to the best possible response. Do not make up any information that is not provided in the context.


        Detail and Conciseness: Provide detailed answers that cater to all aspects of the user's query while keeping the response to the context.

        Important Considerations:

        Accuracy: Ensure all information is accurate and derived from the provided context.
        Completeness: Address all parts of the user's query thoroughly.
        No Assumptions: Avoid making assumptions or adding information not included in the context.

        Refer to the following context in depth.
        
        Context: {context}

        Question: {question}

        In case the context results in same redirect links, or emails, or contact, or any steps that need to be followed, respond properly.
        """

        self.cult_system_prompt = SystemMessagePromptTemplate(
            prompt=PromptTemplate(
                input_variables=["context"],
                template=cult_template_str,
            )
        )

        self.cult_human_prompt = HumanMessagePromptTemplate(
            prompt=PromptTemplate(
                input_variables=["question"],
                template="{question}",
            )
        )

        self.messages = [self.cult_system_prompt, self.cult_human_prompt]

        self.cult_prompt_template = ChatPromptTemplate(
            input_variables=["context", "question"],
            messages=self.messages,
        )

        self.cult_faq_chain = self.create_faq_chain()

    def create_faq_chain(self):
        return {
            "context": answers_retriever,
            "question": RunnablePassthrough()
        } | self.cult_prompt_template | self.chat_model | StrOutputParser()

    def get_chain(self):
        return self.cult_faq_chain

