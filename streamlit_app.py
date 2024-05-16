import streamlit as st

# Initialize the session state if not already done
if 'messages' not in st.session_state:
    st.session_state.messages = []

def add_message(user_message):
    st.session_state.messages.append({"user": user_message, "assistant": f"Response to '{user_message}'"})

st.title("Interactive Chat with Dynamic Updates")

# Chat input for user messages
user_input = st.chat_input("Type your message here...")

# If user has entered a message, process it
if user_input:
    add_message(user_input)

# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message("user"):
        st.write(msg["user"])
    with st.chat_message("assistant"):
        st.write(msg["assistant"])


