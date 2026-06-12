import streamlit as st
import streamlit.components.v1 as components

import os
from dotenv import load_dotenv

from google import genai
from google.genai import types


load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
 
st.set_page_config(page_title="Website Displayer", layout="wide")

st.title("Website Builder")

col1, col2 = st.columns([1,1.2])

if "history" not in st.session_state:
        st.session_state.history=[]

if "current_html" not in st.session_state:
    st.session_state.current_html = ""
with col1:
    st.write("Chat")
    if st.button("Clear Chat & History"):
        
        st.session_state.history = []
        st.rerun()
    
    for message in st.session_state.history:
        if message["role"] == "user":
            role = "user"
        else:
            role = "model"

        with st.chat_message(role):
            text = message["parts"][0]["text"]
            if text.strip().startswith("<!DOCTYPE") or text.strip().startswith("<html"):
                st.write("✅ Website generated — see preview →")
            else:
                st.write(text)
    
    prompt = st.chat_input("Describe your website... ")
    if prompt:
        new_message = {"role":"user","parts":[{"text":prompt}]}
        st.session_state.history.append(new_message)

        with st.chat_message("user"):
            st.write(prompt)
        
        with st.spinner("Building..."):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=st.session_state.history,
                config = types.GenerateContentConfig(
                    system_instruction="""
                        You are a web developer. When asked to build something, 
                        return ONLY complete HTML code with embedded CSS and JS.
                        no explainations, no markdown, no code blocks - just raw HTML
                        starting with <!DOCTYPE html>. DONT PRINT ANYTHING
                        Use href="javascript:void(0)" instead of href="#" for navigation links 
                        to prevent page reload issues, OR use onclick handlers with scrollIntoView.
                    """
                )
            )

            reply = response.text
        
        
        st.session_state.history.append(
            {"role":"model","parts":[{"text":reply}]}
        )

        st.session_state.current_html = reply
        st.rerun()

with col2:
    st.write("Preview")
    preview_container = st.container(height=700,width=600)
    with preview_container:
        components.html(st.session_state.current_html,height=500,scrolling=True)
