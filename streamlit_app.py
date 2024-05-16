import streamlit as st

st.title("Interactive Chat with Dynamic Updates")

# Chat input for user messages
user_input = st.chat_input("Type your message here...")

# If user has entered a message, process it
if user_input:
    add_message(user_input)


