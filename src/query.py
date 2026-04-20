import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Load variables from .env (e.g. GROQ_API_KEY)
load_dotenv()

CHROMA_PERSIST_DIR = os.path.join(os.path.dirname(__file__), '..', 'chroma_db')

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def get_rag_chain():
    # 1. Initialize same embedding model used during indexation
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': False}
    )

    # 2. Load Vector Store (Chroma)
    vector_db = Chroma(
        persist_directory=CHROMA_PERSIST_DIR,
        embedding_function=embeddings
    )
    
    retriever = vector_db.as_retriever(search_kwargs={"k": 5})

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,  # lower temp for more factual answers
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    # 4. Prompt Template
    system_prompt = (
        "Anda adalah asisten virtual cerdas yang bertugas membantu mahasiswa dengan memberikan "
        "informasi terkait pedoman akademik dan kurikulum program studi Teknologi Rekayasa Perangkat Lunak (TRPL). "
        "Gunakan potongan informasi yang diambil dari dokumen akademik di bawah ini untuk menjawab "
        "pertanyaan secara akurat. "
        "Jika terdapat aturan, tabel, atau jadwal, sajikan secara rapi.\n\n"
        "Jika pertanyaan merujuk pada daftar mata kuliah, identifikasi semua mata kuliah yang berada di semester yang sama dan selalu gunakan format Bullet Points. Berikan cetak tebal pada Kode Mata Kuliah.\n\n"
        "Konteks referensi dokumen:\n{context}"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])

    # 5. Build pure LCEL Chain (kompatibel dengan berbagai versi Langchain terbaru)
    rag_chain = (
        {"context": retriever | format_docs, "input": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain

def ask_question(question: str):
    rag_chain = get_rag_chain()
    # Mengembalikan langsung jawaban teks statis
    return rag_chain.invoke(question)

if __name__ == "__main__":
    # Test query saat script dieksekusi secara langsung
    sample_question = "Sebutkan nama dan kode mata kuliah yang ada di semester 1!"
    print(f"User: {sample_question}\n")
    print("AI (Groq):")
    try:
        print(ask_question(sample_question))
    except Exception as e:
        print(f"\nError: {e}\nPastikan GROQ_API_KEY diset di .env dan script indexing.py sudah dijalankan.")
