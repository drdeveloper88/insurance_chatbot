import os
import json
import gradio as gr
from langchain_community.llms import HuggingFaceEndpoint
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import CharacterTextSplitter
from langchain.chains.retrieval_qa.base import RetrievalQA # ✅ updated import path

# --- Set HuggingFace API Token ---
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "xxxxx"  # replace with your own token

# --- Load JSON documents ---
def load_documents(file_path="document.json"):
    """Load all documents from JSON file."""
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [d["content"] for d in data]

# --- Create FAISS vectorstore ---
def create_vectorstore(docs):
    """Create FAISS vectorstore from documents."""
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = splitter.split_text(" ".join(docs))
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.from_texts(texts, embeddings)

# --- Create RetrievalQA chain ---
def create_qa_chain(vectorstore):
    """Create a RetrievalQA chain using HuggingFace Endpoint."""
    llm = HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",  # modern & open LLM on HuggingFace
        temperature=0.5,
        max_new_tokens=256
    )
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        chain_type="stuff"
    )

# --- Load or create FAISS index ---
VECTORSTORE_PATH = "faiss_index"
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

if not os.path.exists(VECTORSTORE_PATH):
    print("🔧 Creating FAISS index...")
    docs = load_documents("document.json")
    vectorstore = create_vectorstore(docs)
    vectorstore.save_local(VECTORSTORE_PATH)
else:
    print("✅ Loading existing FAISS index...")
    vectorstore = FAISS.load_local(
        VECTORSTORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True  # safe if your own index
    )

# --- Create QA Chain ---
qa_chain = create_qa_chain(vectorstore)

# --- Gradio Chat UI ---
def chat(message, history):
    """Handle chat messages."""
    history = history or []
    response = qa_chain.run(message)
    history.append((message, response))
    return "", history

# --- Launch Gradio Interface ---
with gr.Blocks(css=".chatbox {background-color:#f8f9fa; border-radius:15px; padding:10px}", theme=gr.themes.Soft()) as demo:
    gr.Markdown("<h1 style='text-align:center; color:#2b6cb0;'>💬 Smart Insurance Chatbot (JSON Knowledge Base)</h1>")
    chatbot = gr.Chatbot(elem_classes="chatbox")
    msg = gr.Textbox(label="Type your message...")
    clear = gr.Button("Clear Chat")
    msg.submit(chat, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: [], None, chatbot, queue=False)

demo.launch()
