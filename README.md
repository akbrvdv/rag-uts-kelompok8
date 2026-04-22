# 🤖 RAG Starter Pack — UTS Data Engineering

*Retrieval-Augmented Generation — Sistem Informasi Akademik Program Studi TRPL*

-----

## 👥 Identitas Kelompok

| Nama | NIM | Tugas Utama |
| :--- | :--- | :--- |
| Muhammad Akbar Fadilah | 244311051 | Mengolah & menganalisis data jadi insight |
| Raditya Alfareza Purnama Putra | 244311055 | Mengatur proyek & tim supaya berjalan lancar |
| Raihan Firdaus Alfaritsi | 244311055 | Membangun dan mengelola sistem data |

  * **Topik Domain**: Akademik
  * **Stack yang Dipilih**: LangChain
  * **LLM yang Digunakan**: *(Isi nama LLM)*
  * **Vector DB yang Digunakan**: ChromaDB

-----

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

-----

## ⚡ Cara Memulai (Quickstart) Lokal

### 1\. Clone & Setup

```bash
git clone [https://github.com/](https://github.com/)[username]/rag-uts-[kelompok].git
cd rag-uts-[kelompok]

python -m venv venv
source venv/bin/activate        # Linux/Mac
# atau:
venv\Scripts\activate           # Windows

pip install -r requirements.txt
```

### 2\. Konfigurasi API Key

```bash
cp .env.example .env
```

Edit `.env` dan isi API key Anda.
⚠️ **JANGAN commit file .env ke GitHub\!**

### 3\. Siapkan Dokumen

Masukkan dokumen ke folder `data/`

```bash
cp dokumen-saya.pdf data/
```

### 4\. Jalankan Indexing (sekali saja)

```bash
python src/indexing.py
```

### 5\. Jalankan Sistem RAG

#### 🔹 Dengan Streamlit UI

```bash
streamlit run ui/app.py
```

#### 🔹 Atau via CLI

```bash
python src/query.py
```

-----

## 🚀 Panduan Deployment ke Streamlit Community Cloud

Tahapan krusial ini dilakukan dengan prasyarat bahwa kode sumber web, dependencies (`requirements.txt`), serta folder basis memori vektor (`chroma_db`) sudah sukses diunggah (*Push*) ke dalam repositori GitHub Anda.

### Langkah 1: Verifikasi Level Akses Respositori (SANGAT PENTING)

Server aplikasi *Streamlit Cloud* mewajibkan wewenang izin **"Administrator"** terhadap repositori GitHub yang hendak digunakan agar tidak dianggap ilegal/di-*block*.

  * Jika repositori tersebut diciptakan/dimiliki oleh akun GitHub teman Anda, mintalah ia mengizinkan Anda masuk.
  * **Cara untuk teman:** Buka repo GitHub \> Pilih tab **Settings** \> Menu **Collaborators** di sebelah kiri \> cari nama *username* GitHub Anda di daftar **Manage Access** \> Ubah peran (Role) Anda dari tulisan "Write" menjadi **"Admin"**.

### Langkah 2: Tautkan Akun ke Platform Streamlit Cloud

  * Buka browser web Anda dan akses halaman: [https://share.streamlit.io](https://share.streamlit.io)
  * Lakukan Pendaftaran dan/atau *Log In* dengan menyetujui *Single Sign-On* via integrasi akun **GitHub** Anda.

### Langkah 3: Bangun dan Sambungkan Konfigurasi Cloud

  * Sesudah disambungkan, pada dasbor Streamlit, perhatikan dan tekan tombol biru bertuliskan **"New app"** di titik ujung kanan sebelah atas.
  * Platform akan menyeret Anda ke menu **"Deploy an app"**.
  * Di isian **Repository**, pilih/cari nama direktori kelompok proyek RAG kembangan Anda.
  * Biarkan isian rentang **Branch** sesuai asal mulanya (umumnya tertulis `main`).
  * Modifikasi isian direktori bertuliskan **Main file path**: Anda wajib menghapus nama bawaan "*streamlit\_app.py*" tersebut dan ganti dengan akurat menjadi rute file Anda:
    ```text
    ui/app.py
    ```

### Langkah 4: Menanamkan Kunci Brankas (*Secrets / API Key*)

Server cloud sama sekali terisolasi dan belum mengantongi API Key Groq/Gemini/LLM Anda. Kita perlu menyalinnya.

  * Jangan terburu-buru meng-klik tombol *Deploy*\! Di bagian paling bawah, klik tulisan **"Advanced settings"** berlogo gerigi.
  * Sebuah jendela putih / hitam bernama "*Secrets*" akan mencuat. Format sistem menggunakan tata penulisan TOML murni\! Anda **HARUS** mengapit *value* Anda dangan symbol tanda kutip ganda/satu (`"`).
  * Ketik persis seperti teks di bawah ini menyelaraskan dengan API Key orisinal di dalam `.env` lokal Anda:
    ```toml
    GROQ_API_KEY="gsk_xxxxxxxxxxxxxxxxxxxxxx"
    ```

### Langkah 5: Pemasangan Otomatis dan Nikmati Server\!

  * Pencet **'Save'** pada layar *Secrets* tersebut, dan tekan tombol raksasa **'Deploy\!'**.
  * Di pojokan layar web biasanya akan terpampang grafis kompor "*Baking*" atau Terminal Instalasi bergulung. Menandakan virtualisasi VPS sedang mereplikasi modul (`requirements.txt`) Python untuk Anda ke atas peladen dengan sendirinya (kisaran 2-4 menit).
  * Tatkala Terminal mendeteksi '*Successfully built*', tab Anda akan disegarkan mandiri, memaparkan kemegahan Chat UI sistem *Retrieval-Augmented Generation* racikan kelompok Anda\! Web ini sudah di-hosting, *online*, dan link URL uniknya bisa dibagikan ke Dosen serta kawan-kawan.

-----

## ⚙️ Konfigurasi

Semua konfigurasi utama ada di `src/config.py` (atau langsung di setiap file)

| Parameter | Default | Keterangan |
| :--- | :--- | :--- |
| CHUNK\_SIZE | 500 | Ukuran setiap chunk teks (karakter) |
| CHUNK\_OVERLAP | 50 | Overlap antar chunk |
| TOP\_K | 3 | Jumlah dokumen relevan yang diambil |
| MODEL\_NAME | (isi) | Nama model LLM yang digunakan |

-----

## 📊 Hasil Evaluasi

*(Isi setelah pengujian selesai)*

| No | Pertanyaan | Jawaban Sistem | Jawaban Ideal | Skor (1-5) |
| :--- | :--- | :--- | :--- | :--- |
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |

**Rata-rata Skor:** ... <br>
**Analisis:** ...

-----

## 🏗️ Arsitektur Sistem

*(Masukkan gambar diagram arsitektur di sini)*

```text
[Dokumen] → [Loader] → [Splitter] → [Embedding] → [Vector DB]
                                                        ↕
[User Query] → [Query Embed] → [Retriever] → [Prompt] → [LLM] → [Jawaban]
```

-----

## 📚 Referensi & Sumber

  * Framework: (LangChain docs / LlamaIndex docs)
  * LLM: (Groq / Gemini / Ollama)
  * Vector DB: (ChromaDB / FAISS docs)
  * Tutorial yang digunakan: (cantumkan URL)

-----

## 👨‍🏫 Informasi UTS

  * **Mata Kuliah**: Data Engineering
  * **Program Studi**: D4 Teknologi Rekayasa Perangkat Lunak
  * **Deadline**: (isi tanggal)
