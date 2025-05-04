import streamlit as st
import openai
import os

# Load API key
import os
openai.api_key = os.getenv("OPENAI_API_KEY")


# UI
st.set_page_config(page_title="Golf Fitting Chatbot", page_icon="🏌️")
st.title("🏌️ Golf Fitting Chatbot")
st.write("Ask any question about golf club fitting!")

# Input from user
user_input = st.text_input("Your question:")

if user_input:
    with st.spinner("Thinking..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a professional golf club fitter. Answer clearly and helpfully."},
                    {"role": "user", "content": user_input}
                ]
            )
            st.success(response['choices'][0]['message']['content'])
        except Exception as e:
            st.error(f"Error: {e}")
