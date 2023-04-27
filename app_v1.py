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
['API RP 1111 Design Construction Operation and Maintenance of Offshore Hydrocarbon Pipelines (Limit State Design)',
'API RP 2A Recommended Practice for Planning, Designing, and Constructing Fixed Offshore Platforms,
'API RP 2SK 2005 Design and Analysis of Stationkeeping Systems for Floating Structures,
'API STD 53 Well Control Equipment Systems for Drilling Wells,
'API RP 2GEO 2011 Geotechnical and Foundation Design,
'API SP 8C Drilling and Production Hoisting Equipment,
'API SP 6A Specification for Wellhead and Christmas Tree Equipment,
'API RP 2RD Design of Risers for Floating Production Systems (FPSs) and Tension-Leg Platforms (TLPs),
'API SP 5L Pipe Specifications,
'API SP 17J 2014 Specification for Unbonded Flexible Pipe,
'API SP 2B Spec for the fabrication of Structural steel pipe,
'API RP 2GEO 2014 Geotechnical and Foundation Design,
'API STD 1104 1999 Errata 2001 Welding of Pipelines and Related Facilities,
'API RP 2INT-MET Interim Guidance for Assessment of Existing Offshore Structures for Hurricane Conditions,
'API SP 17E 2010 Design and operation of subsea production system subsea umbilicals,
'API Spec 17D Design and Operation of Subsea'])



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
