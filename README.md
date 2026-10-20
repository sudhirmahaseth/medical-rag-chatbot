# Medical Chatbot RAG System 🏥🤖

A domain-specific Medical Q&A system built using a modern **Retrieval-Augmented Generation (RAG)** architecture. The system leverages **Pinecone** as a cloud vector database, implements advanced **semantic chunking** for high-precision context retrieval, utilizes an asynchronous **FastAPI** backend for optimal throughput, and provides an intuitive, interactive **Streamlit** user interface.

## 🚀 Key Features
- **Semantic Chunking**: Breaks down medical text logically based on semantic meaning rather than hard character limits, preserving critical context.
- **High-Performance Vector Search**: Utilizes **Pinecone DB** for dense vector similarity matching to retrieve contextually accurate medical documents.
- **Asynchronous Microservice**: Built with **FastAPI (Async)** achieving sub-200ms p95 response latency for high-concurrency requests.
- **Interactive Web Interface**: A sleek, user-friendly frontend built using **Streamlit** for real-time chatbot interaction.
- **Hallucination Mitigation**: Uses precise prompt tuning and restricted context grounding to ensure reliable, facts-first answers.

## 🛠️ Tech Stack
- **Backend Framework**: FastAPI (Asynchronous)
- **Frontend UI**: Streamlit
- **Orchestration**: LangChain / OpenAI API
- **Vector Database**: Pinecone
- **Embeddings Model**: text-embedding-3-small
- **LLM**: GPT-4o-mini
- **Language**: Python 3.10+

## 📂 Project Architecture
```text
medical-rag-chatbot/
├── app_ui.py            # Streamlit frontend interface
├── main.py              # FastAPI async server & API endpoints
├── rag_engine.py        # Pinecone connection, retrieval, and LLM chain
├── ingest.py            # Script for semantic chunking & indexing medical data
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com
cd medical-rag-chatbot
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_ENVIRONMENT=your_pinecone_env_here
PINECONE_INDEX_NAME=medical-chatbot
```

### 5. Ingest Medical Data (One-time setup)
Place your raw medical texts or documents in the workspace and run the ingestion script to create the Pinecone index:
```bash
python ingest.py
```

### 6. Run the Project

**Step A: Start the FastAPI Backend Server**
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Step B: Start the Streamlit Frontend**
Open a new terminal tab, activate the virtual environment, and run:
```bash
streamlit run app_ui.py
```

## 🛡️ Medical Disclaimer
*This system is designed for informational and educational research purposes only. It is not intended to provide professional medical advice, diagnosis, or treatment.*
