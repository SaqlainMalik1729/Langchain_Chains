from langchain_openai import ChatOpenAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from langchain_core.prompts import load_prompt,PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template= "List five facts about the {topic}",
    input_variables=['topic']
)

model = ChatOpenAI(model='gpt-4.1-mini')

parser = StrOutputParser()

chain = prompt | model 

topic = input("Enter Topic : ")

result = chain.invoke({'topic':topic})
print(result)
