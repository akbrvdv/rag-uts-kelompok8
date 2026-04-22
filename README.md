# 🤖 RAG Starter Pack — UTS Data Engineering

*Retrieval-Augmented Generation — Sistem Informasi Akademik Program Studi TRPL*

Starter pack ini adalah implementasi sistem RAG untuk UTS Data Engineering.
Sistem ini memungkinkan chatbot menjawab pertanyaan berdasarkan dokumen pedoman akademik yang telah di-*index*.

Dibangun menggunakan:
- LangChain  
- LLM Llama 3.1 (via Groq API)  
- Embedding HuggingFace (all-MiniLM-L6-v2)  
- Vector Database ChromaDB  
- Streamlit (Web UI)  

---

## 👥 Identitas Kelompok

| Nama                           | NIM       | Tugas Utama                                  |
| ------------------------------ | --------- | -------------------------------------------- |
| Muhammad Akbar Fadilah         | 244311051 | Mengolah & menganalisis data jadi insight    |
| Raditya Alfareza Purnama Putra | 244311055 | Mengatur proyek & tim supaya berjalan lancar |
| Raihan Firdaus Alfaritsi       | 244311055 | Membangun dan mengelola sistem data          |

* **Topik Domain**: Akademik  
* **Stack yang Dipilih**: LangChain  
* **LLM yang Digunakan**: Llama 3.1 (Groq)  
* **Vector DB yang Digunakan**: ChromaDB  

---

## 📁 Struktur Proyek

```text
rag-uts-kelompok8/
├── data/
│   └── sample.txt
├── src/
│   ├── indexing.py
│   ├── query.py
│   ├── embeddings.py
│   └── utils.py
├── ui/
│   └── app.py
├── chroma_db/               # auto generate setelah indexing
├── docs/
│   └── arsitektur.png
├── evaluation/
│   └── hasil_evaluasi.xlsx
├── notebooks/
│   └── 01_demo_rag.ipynb
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚡ Cara Memulai (Quickstart)

### 1. Clone Repository

```bash
git clone [https://github.com/](https://github.com/)[username]/rag-uts-kelompok8.git
cd rag-uts-kelompok8
```

### 2. Setup Virtual Environment

```bash
python -m venv venv
```

**Aktivasi:**

```bash
# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Konfigurasi API Key

Buat file `.env`:

```bash
cp .env.example .env
```

Isi dengan:

```toml
GROQ_API_KEY="gsk_xxxxxxxxxxxxxx"
```
⚠️ **Jangan commit file .env ke GitHub!**

### 5. Siapkan Dokumen

Masukkan file pedoman akademik ke folder:
```text
data/
```

### 6. Indexing (RAG Ingestion)

⚠️ *Jika sebelumnya sudah pernah indexing, hapus folder `chroma_db/` terlebih dahulu.*

Jalankan:
```bash
python src/indexing.py
```

### 7. Jalankan Sistem RAG

#### 🔹 Streamlit UI
```bash
streamlit run ui/app.py
```
Buka di browser: `http://localhost:8501`

#### 🔹 CLI
```bash
python src/query.py
```

---

## ⚙️ Konfigurasi

| Parameter | Default | Keterangan |
| :--- | :--- | :--- |
| CHUNK_SIZE | 500 | Ukuran setiap chunk teks |
| CHUNK_OVERLAP | 50 | Overlap antar chunk |
| TOP_K | 3 | Jumlah dokumen relevan |
| MODEL_NAME | Llama3 | Model LLM |

---

## 📊 Hasil Evaluasi

*(Isi setelah pengujian selesai)*

| No | Pertanyaan | Jawaban Sistem | Jawaban Ideal | Skor |
| :--- | :--- | :--- | :--- | :--- |
| 1 | ... | ... | ... | ... |

---

## 🏗️ Arsitektur Sistem

```text
[Dokumen] → [Loader] → [Splitter] → [Embedding] → [Vector DB]
                                                         ↓
[User Query] → [Query Embed] → [Retriever] → [Prompt] → [LLM] → [Jawaban]
```

---

## 🚀 Deployment (Streamlit Cloud)

1. Push project ke GitHub
2. Buka [https://share.streamlit.io](https://share.streamlit.io)
3. Login dengan GitHub
4. Klik **New App**
5. Isi detail berikut:
   * **Repository**: repo kamu
   * **Branch**: main
   * **Main file path**: `ui/app.py`
6. Tambahkan **Secrets** (di menu *Advanced Settings* sebelum deploy):
   ```toml
   GROQ_API_KEY="gsk_xxxxx"
   ```
7. Klik **Deploy**

---

## 📚 Referensi & Sumber

* LangChain Documentation
* Groq API
* HuggingFace
* ChromaDB

---

## 👨‍🏫 Informasi UTS

* **Mata Kuliah**: Data Engineering
* **Program Studi**: D4 Teknologi Rekayasa Perangkat Lunak
* **Deadline**: 24 April 2026

---

👍 Menjawab tawaranmu di akhir: Kalau kamu butuh bantuan untuk **mengisi tabel evaluasi dengan contoh metrik yang akademik**, atau mau **bikin diagram arsitekturnya dalam bentuk kode Mermaid/PlantUML** biar tidak cuma teks (lebih pro), kabari saja ya! Aku siap bantu.
