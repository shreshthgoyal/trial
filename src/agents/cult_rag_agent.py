import os
import dotenv
from langchain.agents import (
    create_react_agent,
    Tool,
    AgentExecutor,
)
from langchain import hub
from src.tools.get_price import PriceRetriever
from src.tools.get_gym import GetGym
from src.tools.default import Default
from src.chains.cult_faq_chain import CultFAQChain
from langchain_google_genai import GoogleGenerativeAI
from src.agents.tools_description import ToolDescriptions

class CultAgentExecutor:
    def __init__(self):
        dotenv.load_dotenv()
        self.cult_faq_chain = CultFAQChain().get_chain()
        self.gym_instance = GetGym()
        self.default_instance = Default()
        self.price_instance = PriceRetriever()

        self.tools = [
            Tool(
                name="Queries",
                func=self.cult_faq_chain.invoke,
                description=ToolDescriptions.QUERIES
            ),
            Tool(
                name="Price",
                func=self.price_instance.get_price,
                description=ToolDescriptions.PRICE
            ),
            Tool(
                name="Gym",
                func=self.gym_instance.get_gym,
                description=ToolDescriptions.GYM
            ),
        ]

        self.agent_prompt = hub.pull("hwchase17/react")
        self.agent_chat_model = GoogleGenerativeAI(model=os.getenv("LLM_MODEL"), convert_system_message_to_human=True)
        self.cult_agent = self.create_agent()
        self.cult_agent_executor = self.create_executor()

    def create_agent(self):
        return create_react_agent(
            llm=self.agent_chat_model,
            prompt=self.agent_prompt,
            tools=self.tools,
        )

    def create_executor(self):
        return AgentExecutor(
            agent=self.cult_agent,
            tools=self.tools,
            return_intermediate_steps=False,
            verbose=True,
            handle_parsing_errors=True
        )

    def get_executor(self):
        return self.cult_agent_executor


