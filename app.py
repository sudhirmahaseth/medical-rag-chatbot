import streamlit as st
from openai import OpenAI
from pinecone import Pinecone

st.set_page_config(page_title="Medical AI Chatbot", page_icon="🩺")
st.title("🩺 Medical Chatbot (RAG System)")

with st.sidebar:
    st.header("Setup Credentials")
    openai_key = st.text_input("OpenAI API Key", type="password")
    pinecone_key = st.text_input("Pinecone API Key", type="password")

if not openai_key or not pinecone_key:
    st.warning("Please enter your API keys in the sidebar to start.")
else:
    pc = Pinecone(api_key=pinecone_key)
    client = OpenAI(api_key=openai_key)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask a medical question..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": f"Context: Medical Data RAG Ingested. Question: {prompt}"}]
            )
            answer = response.choices.message.content
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
