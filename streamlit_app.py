import streamlit as st

st.title("Interactive Chat with Dynamic Updates")

# Chat input for user messages
user_input = st.chat_input("Type your message here...")

# Display message
if user_input:
  with st.chat_message("user"):
        st.write(user_input)

