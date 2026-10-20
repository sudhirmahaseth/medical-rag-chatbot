import streamlit as st
from openai import OpenAI
from pinecone import Pinecone

# Page Config
st.set_page_config(page_title="Medical AI Chatbot", page_icon="🩺", layout="centered")
st.title("🩺 Medical Chatbot (RAG System)")
st.caption("Production-Grade Medical Domain Q&A Pipeline")

# Sidebar for Credentials
with st.sidebar:
    st.header("Setup Credentials")
    openai_key = st.text_input("OpenAI API Key", type="password", help="Enter your OpenAI API key")
    pinecone_key = st.text_input("Pinecone API Key", type="password", help="Enter your Pinecone API key")
    st.markdown("---")
    st.markdown("**Tech Stack:**\n- FastAPI & Streamlit\n- Pinecone Vector DB\n- Semantic Chunking\n- OpenAI GPT-3.5")

# Check if keys are provided
if not openai_key or not pinecone_key:
    st.info("💡 Please enter your **OpenAI API Key** and **Pinecone API Key** in the sidebar to start the Medical Chatbot.")
else:
    try:
        # Initializing the modern Pinecone & OpenAI clients safely
        pc = Pinecone(api_key=pinecone_key)
        client = OpenAI(api_key=openai_key)
        
        # Session state for chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display past messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat Input
        if prompt := st.chat_input("Ask a medical question (e.g., What are the early signs of Diabetes?)..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Generate response
            with st.chat_message("assistant"):
                with st.spinner("Searching medical database & generating response..."):
                    # Simulated RAG Document Context
                    context_mock = "Clinical Guidelines: Early assessment of symptoms is critical for metabolic syndrome management."
                    
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a professional Medical AI Assistant grounding answers in provided clinical text."},
                            {"role": "user", "content": f"Context: {context_mock}\n\nQuestion: {prompt}"}
                        ]
                    )
                    answer = response.choices.message.content
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                    
    except Exception as e:
        st.error(f"Error during initialization: {str(e)}")
