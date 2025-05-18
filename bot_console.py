from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

def handle_convo():
    context = ""
    print('Привет! Я - чат-бот! Напишите "выход", чтобы закончить диалог')

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["выход", "пока", "quit", "exit", "bye"]:
            break

        result = chain.invoke({"context": context, "question": user_input})
        print("Bot: ", result)

        context += f"\nUser: {user_input}\nAI: {result}"


model = OllamaLLM(model="gemma3:12b")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

if __name__ == "__main__":
    handle_convo()