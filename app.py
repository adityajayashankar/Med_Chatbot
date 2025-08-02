from flask import Flask, render_template, jsonify, request
from src.helper import download_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq   
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os
import psutil  # 🔹 ADDED
import os

# 🔹 MEMORY CHECK FUNCTION
def log_memory(note=""):
    mem = psutil.Process(os.getpid()).memory_info().rss / (1024 * 1024)
    print(f"[MEMORY] {note}: {mem:.2f} MB")

app = Flask(__name__)
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

log_memory("Before loading embeddings")  # 🔹 ADDED
embeddings = download_embeddings()
log_memory("After loading embeddings")  # 🔹 ADDED

index_name = "med-chatbot-index"

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)
log_memory("After loading Pinecone index")  # 🔹 ADDED

retriever = docsearch.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 1}
)

log_memory("Before loading chat model")  # 🔹 ADDED
chat_model = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="llama3-8b-8192"
)
log_memory("After loading chat model")  # 🔹 ADDED

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])

question_answer_chain = create_stuff_documents_chain(chat_model, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

@app.route('/')
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    log_memory("Before receiving request")
    data = request.get_json()
    msg = data.get("message")
    log_memory("After parsing message")

    response = rag_chain.invoke({"input": msg})
    log_memory("After running RAG chain")

    # ✅ Clear memory if it exists
    if hasattr(rag_chain, "memory") and rag_chain.memory:
        rag_chain.memory.clear()
        print("[MEMORY] Cleared RAG chain memory")

    print(response["answer"])
    return jsonify({"answer": response["answer"]})



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)



