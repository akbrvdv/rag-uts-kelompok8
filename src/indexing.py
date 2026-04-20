import os
import glob
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
CHROMA_PERSIST_DIR = os.path.join(os.path.dirname(__file__), '..', 'chroma_db')

def load_documents():
    docs = []
    
    # Load PDF
    pdf_files = glob.glob(os.path.join(DATA_DIR, "*.pdf"))
    for pdf in pdf_files:
        print(f"Loading PDF: {pdf}")
        loader = PyPDFLoader(pdf)
        docs.extend(loader.load())
        
    # Load TXT
    txt_files = glob.glob(os.path.join(DATA_DIR, "*.txt"))
    for txt_file in txt_files:
        print(f"Loading TXT: {txt_file}")
        try:
            loader = TextLoader(file_path=txt_file, encoding='utf-8')
            docs.extend(loader.load())
        except UnicodeDecodeError:
            print("UTF-8 decoding failed, trying another encoding...")
            loader = TextLoader(file_path=txt_file, encoding='windows-1252')
            docs.extend(loader.load())
            
    return docs

def create_vector_db():
    print("Loading documents...")
    documents = load_documents()
    print(f"Loaded {len(documents)} document pages/rows.")

    # Splitting docs into smaller chunks
    print("Splitting documents...")
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ". ", " "], 
        chunk_size=1500,
        chunk_overlap=100,
        length_function=len
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split into {len(chunks)} chunks.")

    # Initialize HuggingFace embeddings running locally
    print("Initializing HuggingFace Embeddings (all-MiniLM-L6-v2)...")
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': False}
    )

    # Initialize and persist ChromaDB
    print("Creating and saving Chroma Vector DB...")
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PERSIST_DIR
    )
    
    print(f"Successfully generated Vector DB at: {CHROMA_PERSIST_DIR}")

if __name__ == "__main__":
    create_vector_db()