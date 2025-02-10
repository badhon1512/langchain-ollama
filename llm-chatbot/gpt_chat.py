from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
import streamlit as st
from dotenv import load_dotenv

#Env setup
load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_KEY")
os.environ["LANGCHAIN_TRACHING"] = "true"

#preparing the prompt
input_prompt = ChatPromptTemplate.from_messages(
   [
       ("system", "Only provide brief asnwers"),
       ("user" , "{question}")
   ]

)


input_text = st.text_input("Please write, how can i assist:")

# model
model = ChatOpenAI(model = "gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = input_prompt|model|output_parser

st.write(chain.invoke({'question' : input_text}))