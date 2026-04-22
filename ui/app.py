import sys
import os
import streamlit as st

# Ensure we can import from src
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.query import get_rag_chain

st.set_page_config(page_title="Chatbot Pedoman TRPL", page_icon="🎓", layout="centered")

# CSS / Aesthetics Styling
st.markdown("""
<style>
    .user-msg {
        background-color: #2b3a42;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 15px;
    }
    .assistant-msg {
        background-color: #1e2528;
        border-radius: 10px;
        padding: 10px;
        border-left: 3px solid #00ffcc;
        margin-bottom: 15px;
    }
    .header-style {
        text-align: center;
        padding: 1rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='header-style'>Chatbot Pedoman Akademik & Kurikulum TRPL</h1>", unsafe_allow_html=True)
st.caption("Sistem RAG menggunakan Llama 3.1 8B (Groq) dan dokumen akademik D4 TRPL")

# Initialize chat session
if "messages" not in st.session_state:
    st.session_state.messages = []
    
@st.cache_resource
def load_rag_chain_singleton():
    return get_rag_chain()

if "rag_chain" not in st.session_state:
    with st.spinner("Menginisialisasi RAG Chain dan Vector Database..."):
        try:
            st.session_state.rag_chain = load_rag_chain_singleton()
        except Exception as e:
            st.error(f"Gagal memuat sistem: {e}. Pastikan ChromaDB sudah dibuat dan GROQ_API_KEY diset.")

# Render previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Tanyakan sehubungan dengan pedoman akademik atau kurikulum...")

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
        
    # Generate bot response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        with st.spinner("Sedang membaca dokumen dan berpikir..."):
            if "rag_chain" in st.session_state:
                try:
                    answer = st.session_state.rag_chain.invoke(user_input)
                    message_placeholder.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                except Exception as e:
                    st.error(f"Terjadi error: {e}")
            else:
                st.error("RAG Chain tidak diinisialisasi secara benar.")
