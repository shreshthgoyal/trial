import os
from src.agents.cult_rag_agent import CultAgentExecutor

# Possible Queries:
#     "What modes of payment are available?",
#     "Who was the prime minister of india in 2004?",
#     "What gyms I can access through cultpass PRO?",
#     "Can I pause my cultpass?",
#     "What does elite pass offer?",
#     "Is UPI accepted?"
#     "What is the pricing of elite pass?"


def invoke_agent(queries):
    cult_agent_executor_instance = CultAgentExecutor()
    cult_agent_executor = cult_agent_executor_instance.get_executor()

    response = cult_agent_executor.invoke({"input": query})
    print(f"Query: {query}\nResponse: {response['output']}\n")


if __name__ == "__main__":
    print("How can I help you today? 😄 (or type 'exit' to quit): ")
    while True:
        query = input("User: ")
        if query.lower() == 'exit':
            print("Thank you for using CultBot!")
            break
        if(query):
            invoke_agent(query)
        else:
            continue
