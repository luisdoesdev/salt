# from pprint import pprint
import re
# import dotenv
from typing import Any
# from langchain.agents import XMLAgent, tool, AgentExecutor
# from langchain.chat_models import ChatAnthropic
import subprocess
# from langchain.text_splitter import Language
# from langchain.document_loaders.generic import GenericLoader
# from langchain.document_loaders.parsers import LanguageParser

# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.vectorstores import Chroma
# from langchain.embeddings.openai import OpenAIEmbeddings
# import dotenv
# from langchain.vectorstores import Chroma
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.chat_models import ChatOpenAI
# from langchain.memory import ConversationSummaryMemory
# from langchain.chains import ConversationalRetrievalChain
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.text_splitter import (
#     RecursiveCharacterTextSplitter,
#     Language,
# )

# python_splitter = RecursiveCharacterTextSplitter.from_language(language=Language.PYTHON, 
#                                                                chunk_size=2000, 
#                                                                chunk_overlap=200)

# dotenv.load_dotenv()

class OnBoarding:
    def __init__(self) -> None:
        print("Welcome to Salt! I'm your personal assistant.")
        print("To exit, type 'quit'")

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("How can I assist you?")

    def interact(self):
        while True:
            user_input = input("> ")
            if user_input == "quit":
                break
            if user_input == "help":
                print("Available commands: audit, quit, activate, help")
            if user_input == "activate":
                # subprocess.run(["chmod", "-R", "777", "salt"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                subprocess.run("source salt/bin/activate", shell=True)
                print("Salt virtualenv activated!")

            if user_input == "start":
                subprocess.run(["invoke app"], shell=True)
                subprocess.run("echo Salt Server on.", shell=True)
                # subprocess.run(["salt", "master", "-d"])

            if user_input == "audit":
                '''
                ## Prerequisites

                    ## Installation
                    1. Install virtualenv `pip install virtualenv`
                    2. create virtualenv `virtualenv -p python3 salt`
                    3. activate virtualenv `source salt/bin/activate` Fig:1.1
                    4. Install invoke `pip install invoke`
                    5. Install dependencies `invoke install`
                '''
                # agent = XMLAgent.from_file("onboarding.xml")
                # executor = AgentExecutor(agent)
                # executor.run()
                # Install virtualenv
                
                # continue
                subprocess.run(["echo", "Updating Salt..."])
                # subprocess.run(["pip3", "install", "virtualenv"])
                # subprocess.run(["virtualenv", "-p", "python3", "salt"])
                # # subprocess.run(["chmod", "-R", "777", "salt"])
                # # subprocess.run(["source", "salt/bin/activate"])
                # subprocess.run("source salt/bin/activate", shell=True)
                # subprocess.run(["pip3", "install", "invoke"])
                # subprocess.run(["invoke", "install"])

                subprocess.run(["pip3", "install", "virtualenv"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                subprocess.run(["virtualenv", "-p", "python3", "salt"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                subprocess.run(["chmod", "-R", "777", "salt"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                subprocess.run("source salt/bin/activate", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                subprocess.run(["pip3", "install", "invoke"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                subprocess.run(["invoke", "install"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


                response = self.process_input(user_input)
                # once audit is done, we need to exit the program and activate the virtualenv
                subprocess.run(["source salt/bin/activate"])
                
                print(response)

    def chat(self, question):
        # Process the user's input and return a response
        
        return  'You said: {question}}'

    def process_input(self, user_input):
        # Process the user's input and return a response
        # print("Processing input...")
        return f"You said: {user_input}"
    
    

if __name__ == "__main__":
    onboarding = OnBoarding()
    onboarding.interact()


# loader = GenericLoader.from_filesystem(
#     "/Users/luistorruella/salt",
#     glob="*",
#     suffixes=[".py", '.js'],
#     parser=LanguageParser(language=Language.PYTHON, parser_threshold=500),
# )
# docs = loader.load()

# texts = python_splitter.split_documents(docs)
# python_splitter = RecursiveCharacterTextSplitter.from_language(language=Language.PYTHON, 
#                                                                chunk_size=2000, 
#                                                              chunk_overlap=200)
# texts = python_splitter.split_documents(docs)
# db = Chroma.from_documents(texts, OpenAIEmbeddings(disallowed_special=()))
# retriever = db.as_retriever(
#     search_type="mmr", # Also test "similarity"
#     search_kwargs={"k": 8},
# )

# dotenv.load_dotenv()

# db = Chroma.from_documents(texts, OpenAIEmbeddings(disallowed_special=()))
# retriever = db.as_retriever(
#     search_type="mmr", # Also test "similarity"
#     search_kwargs={"k": 8},
# )

# llm = ChatOpenAI(model="gpt-4") 
# memory = ConversationSummaryMemory(llm=llm,memory_key="chat_history",return_messages=True)
# qa = ConversationalRetrievalChain.from_llm(llm, retriever=retriever, memory=memory)

# question = "How can I initialize salt app?"
# result = qa(question)
# result['answer']
