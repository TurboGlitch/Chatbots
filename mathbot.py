import streamlit as st

import os
from dotenv import load_dotenv

from google import genai
from google.genai import types

import time

load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
 
st.set_page_config(page_title="Math Chatbot", layout="wide")

st.title("Math Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

with st.sidebar:
    st.html("""
        <style>
        [data-testid="stSidebarContent"] h1 {
            color: lightblue;
            font-size: 1.5rem;
            font-weight: 550;
            letter-spacing: 0.05em;
            height: 80px;
            margin-top: -40px;
        }
        </style>
    """)
    st.title("⚙️ Settings")
    st.html("""
            <style>
            [data-testid="stSidebarContent"] button {
                background-color: transparent;
                color: #b0b0b0;
                border: 0px;
                width: 100%;
            }
            
            [data-testid="stSidebarContent"] button:hover {
                background-color: #3a3a3a;
                color: #e0e0e0;
                border: 0px;
                padding: 4px 12px;
            }
            </style>
        """)
    if st.button("Clear Chat",type="tertiary"):
        
        st.session_state.history = []
        st.rerun()




for message in st.session_state.history:
    role = "user" if message["role"] == "user" else "assistant"
    with st.chat_message(role):
        st.write(message["parts"][0]["text"])


if prompt := st.chat_input("Ask a math question"):
    st.session_state.history.append(
    {"role" : "user", "parts": [{"text" : prompt}]}
    )

    with st.chat_message("user"):
        st.write(prompt)


    with st.spinner("Thinking..."):
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite-preview",
            contents=st.session_state.history,
            config=types.GenerateContentConfig(
                system_instruction="""
                    You are a chatbot who helps users in all types of maths.  
                    Don't talk about anything else and be polite.
                    """
            )
        )


        reply = response.text

    
    

    with st.chat_message("assistant"):
        st.write(reply)
    
    st.toast("Success",icon="✅",duration=1)

    st.session_state.history.append(
        {"role":"model", "parts":[{"text":reply}]}
    )
    
