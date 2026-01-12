
import streamlit as st
import openai

# Set OpenAI API key
openai.api_key = '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'

st.title("ChatGPT-like Chatbot")

# Get user input
user_input = st.text_input("You:")

if user_input:
    # Call OpenAI API
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=user_input,
        max_tokens=150
    )
    # Show response
    st.write("Bot:", response.choices[0].text.strip())
