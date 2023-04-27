#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-
#Document Chatbot - Upload documents (docx files) and let the ChatBot do the reading for you. 
#You just need to ask the ChatBot questions and it will answer. 

import streamlit as st
import docx2txt
import openai
import llama_index
import langchain

from io import BytesIO
from llama_index import SimpleDirectoryReader
from llama_index import download_loader
from llama_index import GPTListIndex, LLMPredictor, GPTSimpleVectorIndex, PromptHelper
from langchain import OpenAI
from langchain.chat_models import ChatOpenAI


import os
os.environ['OPENAI_API_KEY'] = "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"

model_engine = "text-davinci-003"
openai.api_key = "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"

st.title("Document Chatbot")
st.sidebar.header("Instructions")
st.sidebar.info(
    '''Upload a **Document(.docx)** and let **ChatGPT** answer any questions you have about contents of the document.'''
    )
uploaded_files = st.file_uploader('Upload your file',accept_multiple_files=True, type=['docx'])

documents = []
if uploaded_files is not None:
  for file in uploaded_files:
        bytes_data = file.read()
        file_object = BytesIO(bytes_data)
        rawtext = docx2txt.process(file_object)
        doc = llama_index.Document(rawtext)
        documents.append(doc)

def docu_chat(user_query):
    # define LLM
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.5, model_name="text-davinci-003"))

    # define prompt helper
    # set maximum input size
    max_input_size = 4096
    # set number of output tokens
    num_output = 256
    # set maximum chunk overlap
    max_chunk_overlap = 20
    prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)
    custom_LLM_index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    # Query your index!
    response = custom_LLM_index.query(user_query,response_mode="compact")
    st.write(f"<b>{response}</b>",unsafe_allow_html=True)
    #st.write(response)
    
user_query = st.text_input("Enter your query here:q", "")

import tenacity
try:
    docu_chat(user_query)
except tenacity.RetryError:
    # Handle the error or suppress it
    pass