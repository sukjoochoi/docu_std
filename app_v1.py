#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#App to query ChatGPT on specific Industry standards and codes

import streamlit as st
import openai
import pandas as pd


# Set the model engine and your OpenAI API key
model_engine = "text-davinci-003"
openai.api_key = "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"


st.title("Codes and Standards Q & A")
st.sidebar.header("Instructions")
st.sidebar.info(
    '''Select the Code or Standard about which you have a question. Then
       enter a **query** in the **text box** and press the **Fetch Answer** button to receive 
       a **response**
       '''
    )


options = st.multiselect('Select the Code(s)/Standard(s) about which you have a Question',
                         ['ASME Sec VIII: Boiler and Pressure Vessel Code',
                         'API 660: Shell and Tube Heat Exchnagers',
                         'API 661: Air Cooled Heat Exchangers',
                         'API 662: Plate and Frame Heat Exchangers ',
                         'API 668: Brazed Aluminum Exchangers',
                         'API 612: Steam Turbines',
                         'API 616: Gas Turbines',
                         'API 617: Axial, Centrifugal and Expander Compressors',
                         'API 618: Reciprocating compressors',
                         'API 619: Rotary Compressors',
                         'API 681: Liquid Ring Vacuum Pumps and Compressors',
                         'API 672: Centrifugal Air Compressors',
                         'API 610: Centrifugal Pumps',
                         'API 685: Seal-less Centrifugal Pumps',
                         'API 686: Recommended Practice for Machinery Installation and Installation Design',
                         'API 674: Positive Displacement Pumps - Reciprocating',
                         'API 675: Positive Displacement Pumps - Controlled Volume',
                         'API 676: Positive Displacement Pumps - Rotary',
                         'API 682: Pumps - Shaft Sealing Systems for Centrifugal and Rotary Pumps',
                         'ASME PTC 8.2: Centrifugal Pumps',
                         'ASME B73.1: Specification for Horizontal End Suction Centrifugal Pumps',
                         'ASME B73.2: Specification for Vertical In-Line Centrifugal Pumps',
                         'ASME B73.3: Specification for Sealless Horizontal End Suction Centrifugal Pumps',
                         'ASME PTC 18: Hydraulic Turbines and Pump-Turbines',
                         'NACE: MR0175 - Petroleum and Natural Gas Industries — Materials for use in H2S-containing environments',
                         'NFPA 59A: Standard for the Production, Storage, and Handling of Liquefied Natural Gas (LNG)'])



def ChatGPT(user_query):

    # Use the OpenAI API to generate a response
    completion = openai.Completion.create(
                                  engine = model_engine,
                                  prompt = user_query,
                                  max_tokens = 1024,
                                  n = 1,
                                  temperature = 0.01,
                                      )
    response = completion.choices[0].text
    return response



def main():

    # Get user input
    user_query = st.text_input("Enter your query here:q", "")

    #st.button("Enter", key="codes", help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False)
    if st.button("Fetch Answer"):
        if user_query != ":q" or user_query != "":
            # Pass the query to the ChatGPT function
            response = ChatGPT(f"""{user_query}. Use information only from these 
                                code(s)/standard(s): {options} to answer.""")
            return st.write(f"{response}")


# call the main function
main() 