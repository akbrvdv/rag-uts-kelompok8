# 🤖 RAG Starter Pack — UTS Data Engineering

*Retrieval-Augmented Generation — Sistem Tanya-Jawab Cerdas Berbasis Dokumen*

Starter pack ini adalah kerangka awal proyek RAG untuk UTS Data Engineering D3/D4.
Mahasiswa mengisi, memodifikasi, dan mengembangkan kode ini sesuai topik kelompok masing-masing.

---

## 👥 Identitas Kelompok

| Nama                           | NIM       | Tugas Utama                                  |
| ------------------------------ | --------- | -------------------------------------------- |
| Muhammad Akbar Fadilah         | 244311051 | Mengolah & menganalisis data jadi insight    |
| Raditya Alfareza Purnama Putra | 244311055 | Mengatur proyek & tim supaya berjalan lancar |
| Raihan Firdaus Alfaritsi       | 244311055 | Membangun dan mengelola sistem data          |

* **Topik Domain**: (Akademik / Kesehatan / Hukum / Bisnis / Pertanian / Teknologi)
* **Stack yang Dipilih**: (LangChain / LlamaIndex / From Scratch)
* **LLM yang Digunakan**: (Groq / Gemini / Ollama / lainnya)
* **Vector DB yang Digunakan**: (ChromaDB / FAISS / lainnya)

---

## 📁 Struktur Proyek

```
rag-uts-[nama-kelompok]/
├── data/
│   └── sample.txt                # Dokumen sumber Anda (PDF, TXT, dll.)
├── src/
│   ├── indexing.py              # 🔧 WAJIB DIISI: Pipeline indexing
│   ├── query.py                 # 🔧 WAJIB DIISI: Pipeline query & retrieval
│   ├── embeddings.py            # 🔧 WAJIB DIISI: Konfigurasi embedding
│   └── utils.py                 # Helper functions
├── ui/
│   └── app.py                   # 🔧 WAJIB DIISI: Antarmuka Streamlit
├── docs/
│   └── arsitektur.png           # 📌 Diagram arsitektur (buat sendiri)
├── evaluation/
│   └── hasil_evaluasi.xlsx      # 📌 Tabel evaluasi 10 pertanyaan
├── notebooks/
│   └── 01_demo_rag.ipynb        # Notebook demo
├── .env.example                 # Template environment variables
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚡ Cara Memulai (Quickstart)

### 1. Clone & Setup

```bash
git clone https://github.com/[username]/rag-uts-[kelompok].git
cd rag-uts-[kelompok]

python -m venv venv
source venv/bin/activate        # Linux/Mac
# atau:
venv\Scripts\activate           # Windows

pip install -r requirements.txt
```

---

### 2. Konfigurasi API Key

```bash
cp .env.example .env
```

Edit `.env` dan isi API key Anda
⚠️ **JANGAN commit file .env ke GitHub!**

---

### 3. Siapkan Dokumen

Masukkan dokumen ke folder `data/`

```bash
cp dokumen-saya.pdf data/
```

---

### 4. Jalankan Indexing (sekali saja)

```bash
python src/indexing.py
```

---

### 5. Jalankan Sistem RAG

#### 🔹 Dengan Streamlit UI

```bash
streamlit run ui/app.py
```

#### 🔹 Atau via CLI

```bash
python src/query.py
```

---

## ⚙️ Konfigurasi

Semua konfigurasi utama ada di `src/config.py` (atau langsung di setiap file)

| Parameter     | Default | Keterangan                          |
| ------------- | ------- | ----------------------------------- |
| CHUNK_SIZE    | 500     | Ukuran setiap chunk teks (karakter) |
| CHUNK_OVERLAP | 50      | Overlap antar chunk                 |
| TOP_K         | 3       | Jumlah dokumen relevan yang diambil |
| MODEL_NAME    | (isi)   | Nama model LLM yang digunakan       |

---

## 📊 Hasil Evaluasi

*(Isi setelah pengujian selesai)*

| No | Pertanyaan | Jawaban Sistem | Jawaban Ideal | Skor (1-5) |
| -- | ---------- | -------------- | ------------- | ---------- |
| 1  | ...        | ...            | ...           | ...        |
| 2  | ...        | ...            | ...           | ...        |

**Rata-rata Skor:** ...
**Analisis:** ...

---

## 🏗️ Arsitektur Sistem

*(Masukkan gambar diagram arsitektur di sini)*

```
[Dokumen] → [Loader] → [Splitter] → [Embedding] → [Vector DB]
                                                         ↕
[User Query] → [Query Embed] → [Retriever] → [Prompt] → [LLM] → [Jawaban]
```

---

## 📚 Referensi & Sumber

* Framework: (LangChain docs / LlamaIndex docs)
* LLM: (Groq / Gemini / Ollama)
* Vector DB: (ChromaDB / FAISS docs)
* Tutorial yang digunakan: (cantumkan URL)

---

## 👨‍🏫 Informasi UTS

* **Mata Kuliah**: Data Engineering
* **Program Studi**: D4 Teknologi Rekayasa Perangkat Lunak
* **Deadline**: (isi tanggal)
