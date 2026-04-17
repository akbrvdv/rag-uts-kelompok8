🤖 RAG Starter Pack — UTS Data Engineering
Retrieval-Augmented Generation — Analisis Variabilitas Cuaca Historis Kecamatan Taman, Kota Madiun Berbasis Open-Meteo API

👥 Identitas Kelompok
Nama	NIM	Tugas Utama
Raihan Firdaus Alfaritsi	244311055	Membangun dan mengelola sistem data
Muhammad Akbar Fadilah	244311051	Mengolah & menganalisis data jadi insight
Raditya Alfareza Purnama Putra	244311054 Mengatur proyek & tim supaya berjalan lancar

Topik Domain: Lingkungan
Stack yang Dipilih: LangChain
LLM yang Digunakan: 
Vector DB yang Digunakan: 

🗂️ Struktur Proyek
rag-uts-[nama-kelompok]/
├── data/                    # Dokumen sumber Anda (PDF, TXT, dll.)
│   └── sample.txt           # Contoh dokumen (ganti dengan dokumen Anda)
├── src/
│   ├── indexing.py          # 🔧 WAJIB DIISI: Pipeline indexing
│   ├── query.py             # 🔧 WAJIB DIISI: Pipeline query & retrieval
│   ├── embeddings.py        # 🔧 WAJIB DIISI: Konfigurasi embedding
│   └── utils.py             # Helper functions
├── ui/
│   └── app.py               # 🔧 WAJIB DIISI: Antarmuka Streamlit
├── docs/
│   └── arsitektur.png       # 📌 Diagram arsitektur (buat sendiri)
├── evaluation/
│   └── hasil_evaluasi.xlsx  # 📌 Tabel evaluasi 10 pertanyaan
├── notebooks/
│   └── 01_demo_rag.ipynb    # Notebook demo dari hands-on session
├── .env.example             # Template environment variables
├── .gitignore
├── requirements.txt
└── README.md

⚡ Cara Memulai (Quickstart)
1. Clone & Setup
# Clone repository ini
git clone https://github.com/akbrvdv/rag-uts-kelompok8.git
cd rag-uts-kelompok8

# Buat virtual environment
python -m venv venv
source venv/bin/activate        # Linux/Mac
# atau: venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
2. Konfigurasi API Key
# Salin template env
cp .env.example .env

# Edit .env dan isi API key Anda
# JANGAN commit file .env ke GitHub!
3. Siapkan Dokumen
Letakkan dokumen sumber Anda di folder data/:

# Contoh: salin PDF atau TXT ke folder data
cp dokumen-saya.pdf data/
4. Jalankan Indexing (sekali saja)
python src/indexing.py
5. Jalankan Sistem RAG
# Dengan Streamlit UI
streamlit run ui/app.py

# Atau via CLI
python src/query.py

🔧 Konfigurasi
Semua konfigurasi utama ada di src/config.py (atau langsung di setiap file):

Parameter	Default	Keterangan
CHUNK_SIZE	500	Ukuran setiap chunk teks (karakter)
CHUNK_OVERLAP	50	Overlap antar chunk
TOP_K	3	Jumlah dokumen relevan yang diambil
MODEL_NAME	(isi)	Nama model LLM yang digunakan
📊 Hasil Evaluasi
(Isi setelah pengujian selesai)

#	Pertanyaan	Jawaban Sistem	Jawaban Ideal	Skor (1-5)
1	...	...	...	...
2	...	...	...	...
Rata-rata Skor: ...
Analisis: ...

🏗️ Arsitektur Sistem
(Masukkan gambar diagram arsitektur di sini)

[Dokumen] → [Loader] → [Splitter] → [Embedding] → [Vector DB]
                                                         ↕
[User Query] → [Query Embed] → [Retriever] → [Prompt] → [LLM] → [Jawaban]

📚 Referensi & Sumber
Framework: (LangChain docs / LlamaIndex docs)
LLM: (Groq / Gemini / Ollama)
Vector DB: (ChromaDB / FAISS docs)
Tutorial yang digunakan: (cantumkan URL)

👨‍🏫 Informasi UTS
Mata Kuliah: Data Engineering
Program Studi: D4 Teknologi Rekayasa Perangkat Lunak
Deadline: (isi tanggal)
