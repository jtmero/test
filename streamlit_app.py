import streamlit as st
import time

# A function to simulate dynamic content update
def update_chat():
    if 'messages' not in st.session_state:
        st.session_state.messages = []
        
    with st.chat_message("user"):
        st.write(f"User message {len(st.session_state.messages) + 1}")
        
    with st.chat_message("assistant"):
        st.write(f"Assistant response {len(st.session_state.messages) + 1}")

    # Append the new message to the session state
    st.session_state.messages.append(f"Message {len(st.session_state.messages) + 1}")

# Main Streamlit app code
st.title("Chat with Dynamic Content")

if st.button("Add Message"):
    update_chat()

# Display existing messages
for msg in st.session_state.get('messages', []):
    with st.chat_message("user"):
        st.write(msg)
        
    with st.chat_message("assistant"):
        st.write(f"Response to {msg}")

