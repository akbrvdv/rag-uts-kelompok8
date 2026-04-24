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
| CHUNK_SIZE | 1500 | Ukuran setiap chunk teks |
| CHUNK_OVERLAP | 100 | Overlap antar chunk |
| TOP_K | 3 | Jumlah dokumen relevan |
| MODEL_NAME | Llama3 | Model LLM |

---

## 📊 Hasil Evaluasi

Berikut adalah hasil pengujian sistem RAG terhadap beberapa pertanyaan seputar akademik:

| No | Pertanyaan | Jawaban Sistem | Jawaban Ideal | Skor |
| :--- | :--- | :--- | :--- | :--- |
| 1 | apa saja pedoman TRPL? | Pedoman Akademik Program Studi Teknologi Rekayasa Perangkat Lunak (TRPL) tidak secara eksplisit disebutkan dalam dokumen yang disediakan... | Pedoman TRPL meliputi aturan-aturan serta kebutuhan akademis dalam ruang lingkup PNM... | 4 |
| 2 | apa itu krs? | KRS adalah singkatan dari "Kartu Rencana Studi"... Dokumen yang digunakan untuk merekam rencana studi mahasiswa dalam satu semester atau lebih. | KRS adalah dokumen yang digunakan untuk merekam rencana studi mahasiswa dalam satu semester atau lebih. | 5 |
| 3 | berapa SKS mata kuliah Data Engineering di program studi TRPL? | Mata kuliah Data Engineering memiliki bobot 0 SKS Teori dan 2 SKS Praktik. | Mata kuliah Data Engineering pada kurikulum 2025/2026 terdiri dari 2 SKS Praktik. | 5 |
| 4 | apa kepanjangan dari TRPL? | TRPL adalah singkatan dari Teknologi Rekayasa Perangkat Lunak. | TRPL adalah singkatan dari Teknologi Rekayasa Perangkat Lunak... di Politeknik Negeri Madiun. | 4 |
| 5 | bagaimana prosedur untuk cuti akademik | Prosedur untuk cuti akademik dapat dilihat pada Pedoman Akademik PNM 2024... Mengambil formulir permohonan cuti, mengisi formulir, dsb. | Prosedur: Mengambil formulir permohonan cuti di Sub Bag Akademik dan Kemahasiswaan, Formulir diisi dengan benar, dan sudah disetujui... | 5 |
| 6 | Bagaimana prinsip penyelenggaraan Program MBKM PNM? | Menurut Pedoman Akademik PNM 2024, mahasiswa diberikan hak mengikuti program MBKM, memperoleh konversi maksimal 20 SKS. | MBKM adalah program Merdeka Belajar Kampus Merdeka dengan konversi maksimal 20 SKS per semester. | 5 |
| 7 | Bagaimana penilaian pada Nilai Evaluasi Perkuliahan? | Nilai Evaluasi Perkuliahan dinyatakan dalam bentuk markah mentah rentang 0-100 dari partisipasi, tugas, UTS, dan UAS. | Sistem penilaian menggunakan huruf mutu A, AB, B, BC, C, D, dan E berdasarkan akumulasi tugas, UTS, dan UAS. | 4 |
| 8 | Apa saja predikat kelulusan di prodi TRPL? | Predikat kelulusan terdiri dari Pujian (IPK >3,50), Sangat Memuaskan (3,01-3,50), Memuaskan (2,76-3,00), dan Lulus (2,00-2,75). | Predikat kelulusan terdiri dari Memuaskan, Sangat Memuaskan, dan Dengan Pujian (Cum Laude) sesuai IPK akhir. | 5 |
| 9 | Bagaimana penyelenggaraan evaluasi perkuliahan di setiap semesternya? | Meliputi UTS pada minggu ke-8, UAS pada minggu ke-16, unjuk kerja/proyek, tugas, dan kuis. | Evaluasi dilakukan tiap semester melalui tugas, kuis, proyek, UTS, dan UAS. | 4 |
| 10 | Bagaimana akademis menghitung nilai indeks prestasi semester | Indeks Prestasi Semester (IPS) dihitung dari nilai rata-rata akhir semester gabungan seluruh mata kuliah yang ditempuh. | IPS dihitung berdasarkan total bobot nilai mata kuliah dibagi total SKS yang diambil pada semester tersebut. | 4 |

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
