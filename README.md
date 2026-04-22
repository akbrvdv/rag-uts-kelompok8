```markdown
# 🤖 RAG Starter Pack — UTS Data Engineering  
*Retrieval-Augmented Generation — Sistem Informasi Akademik TRPL*

Proyek ini merupakan implementasi sistem **Retrieval-Augmented Generation (RAG)** berbasis dokumen pedoman akademik Program Studi TRPL. Sistem ini memungkinkan chatbot menjawab pertanyaan berdasarkan dokumen yang telah di-*index*.

Dibangun menggunakan:
- LangChain  
- LLM Llama 3.1 (via Groq API)  
- Embedding HuggingFace (all-MiniLM-L6-v2)  
- Vector Database ChromaDB  
- Streamlit (Web UI)  

---

## 👥 Identitas Kelompok

| Nama                           | NIM       | Peran                                      |
| ------------------------------ | --------- | ------------------------------------------ |
| Muhammad Akbar Fadilah         | 244311051 | Data processing & insight                  |
| Raditya Alfareza Purnama Putra | 244311055 | Project management                         |
| Raihan Firdaus Alfaritsi       | 244311055 | System & data engineering                  |

- Topik Domain: Akademik  
- Framework: LangChain  
- LLM: Llama 3.1 (Groq)  
- Vector DB: ChromaDB  

---

## 📁 Struktur Proyek

```

rag-uts-kelompok8/
├── data/
├── src/
│   ├── indexing.py
│   ├── query.py
│   ├── embeddings.py
│   └── utils.py
├── ui/
│   └── app.py
├── chroma_db/
├── docs/
├── evaluation/
├── notebooks/
├── .env.example
├── requirements.txt
└── README.md

````

---

## ⚡ Cara Menjalankan

### 1. Clone Repository
```bash
git clone https://github.com/[username]/rag-uts-kelompok8.git
cd rag-uts-kelompok8
````

### 2. Setup Virtual Environment

```bash
python -m venv venv
```

Aktivasi:

Windows:

```bash
venv\Scripts\activate
```

PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

Linux/Mac:

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup API Key (WAJIB)

Buat file `.env` lalu isi:

```bash
GROQ_API_KEY="gsk_xxxxxxxxx"
```

⚠️ Jangan commit `.env` ke GitHub

---

### 5. Masukkan Dokumen

Masukkan file pedoman akademik ke folder:

```
data/
```

---

### 6. Indexing (RAG Ingestion)

⚠️ Jika sebelumnya sudah pernah indexing:

* hapus folder `chroma_db/`

Jalankan:

```bash
python src/indexing.py
```

---

### 7. Jalankan Aplikasi

#### Streamlit (UI)

```bash
streamlit run ui/app.py
```

Buka di browser:

```
http://localhost:8501
```

#### CLI

```bash
python src/query.py
```

---

## ⚙️ Konfigurasi

| Parameter     | Default | Keterangan             |
| ------------- | ------- | ---------------------- |
| CHUNK_SIZE    | 500     | Ukuran potongan teks   |
| CHUNK_OVERLAP | 50      | Overlap antar chunk    |
| TOP_K         | 3       | Jumlah hasil retrieval |
| MODEL_NAME    | Llama3  | Model LLM              |

---

## 🧠 Cara Kerja Sistem

```
Dokumen → Chunking → Embedding → ChromaDB
                                      ↓
User Query → Embedding → Retriever → LLM → Jawaban
```

---

## 🚀 Deployment (Streamlit Cloud)

1. Push project ke GitHub
2. Buka [https://share.streamlit.io](https://share.streamlit.io)
3. Login dengan GitHub
4. Klik "New App"
5. Isi:

   * Repository: repo kamu
   * Branch: main
   * Main file path:

     ```
     ui/app.py
     ```
6. Tambahkan Secrets:

   ```
   GROQ_API_KEY="gsk_xxxxx"
   ```
7. Klik Deploy

---

## 📊 Evaluasi

| No | Pertanyaan | Jawaban Sistem | Jawaban Ideal | Skor |
| -- | ---------- | -------------- | ------------- | ---- |
| 1  | ...        | ...            | ...           | ...  |

---

## 📚 Referensi

* LangChain
* Groq API
* HuggingFace
* ChromaDB

---

## 👨‍🏫 Informasi UTS

* Mata Kuliah: Data Engineering
* Program Studi: D4 Teknologi Rekayasa Perangkat Lunak
* Tugas: Implementasi Sistem RAG

---
