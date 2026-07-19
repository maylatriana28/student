# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan tinggi yang telah berdiri sejak tahun 2000 dan telah menghasilkan banyak lulusan dengan reputasi yang baik. Namun, institusi ini masih menghadapi permasalahan berupa mahasiswa yang tidak menyelesaikan pendidikannya atau mengalami dropout.

Tingginya jumlah mahasiswa yang mengalami dropout dapat memberikan dampak terhadap keberhasilan akademik mahasiswa maupun performa institusi. Oleh karena itu, diperlukan analisis terhadap karakteristik mahasiswa untuk mengetahui faktor-faktor yang berkaitan dengan dropout serta sebuah sistem prediksi yang dapat membantu mengidentifikasi mahasiswa yang berpotensi mengalami dropout.

Proyek ini menggunakan pendekatan data science untuk menganalisis data mahasiswa, membangun model machine learning untuk memprediksi status mahasiswa, serta membuat business dashboard yang dapat digunakan untuk membantu Jaya Jaya Institut dalam memonitor kondisi mahasiswa.

### Permasalahan Bisnis

Permasalahan bisnis yang ingin diselesaikan dalam proyek ini adalah:

1. Berapa jumlah dan persentase mahasiswa yang mengalami dropout?
2. Faktor apa saja yang berkaitan dengan tingginya tingkat dropout mahasiswa?
3. Bagaimana kondisi pembayaran biaya pendidikan dan status debtor berkaitan dengan tingkat dropout?
4. Bagaimana penerimaan beasiswa berkaitan dengan tingkat dropout mahasiswa?
5. Bagaimana usia mahasiswa saat pertama kali mendaftar berkaitan dengan tingkat dropout?
6. Bagaimana performa akademik mahasiswa pada semester pertama berkaitan dengan risiko dropout?
7. Bagaimana tingkat dropout berbeda pada masing-masing program studi atau course?
8. Bagaimana machine learning dapat digunakan untuk membantu memprediksi status mahasiswa?

### Cakupan Proyek

Proyek ini mencakup beberapa tahapan utama, yaitu:

- Memahami karakteristik dan struktur dataset mahasiswa.
- Melakukan pemeriksaan kualitas data, seperti missing value dan data duplikat.
- Melakukan exploratory data analysis untuk memahami distribusi data.
- Melakukan data preparation dan preprocessing.
- Membagi data menjadi data training dan testing.
- Membangun beberapa model machine learning.
- Membandingkan performa model menggunakan metrik evaluasi klasifikasi.
- Memilih dan menyimpan model terbaik dalam bentuk pipeline.
- Membuat aplikasi prediksi status mahasiswa menggunakan Streamlit.
- Membuat business dashboard menggunakan Metabase.
- Memberikan kesimpulan dan rekomendasi tindakan berdasarkan hasil analisis.

## Persiapan

### Sumber Data

Dataset yang digunakan dalam proyek ini adalah **Students Performance Dataset** yang disediakan oleh Dicoding.

Dataset dapat diakses melalui:

https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Dataset terdiri dari **4.424 data mahasiswa dan 37 kolom**, yang mencakup informasi mengenai:

- Karakteristik demografi mahasiswa.
- Latar belakang pendidikan.
- Kondisi sosial dan ekonomi.
- Status pembayaran biaya pendidikan.
- Status beasiswa.
- Performa akademik semester pertama dan kedua.
- Kondisi ekonomi makro.
- Status akhir mahasiswa.

Target yang digunakan adalah kolom `Status`, yang terdiri dari tiga kategori:

- `Graduate`
- `Dropout`
- `Enrolled`

Distribusi target pada dataset adalah:

| Status | Jumlah |
|---|---:|
| Graduate | 2.209 |
| Dropout | 1.421 |
| Enrolled | 794 |
| **Total** | **4.424** |

### Setup Environment

Pastikan Python telah terinstal pada perangkat. Proyek ini menggunakan Python 3.10.

Buka terminal atau Command Prompt, kemudian masuk ke direktori proyek:

```bash
cd submission
```

Buat virtual environment:

```bash
python -m venv venv
```

Aktifkan virtual environment pada Windows:

```bash
venv\Scripts\activate
```

Untuk macOS/Linux:

```bash
source venv/bin/activate
```

Instal seluruh library yang diperlukan:

```bash
python -m pip install -r requirements.txt
```

### Menjalankan Notebook

Untuk menjalankan proses analisis dan modeling, jalankan Jupyter Notebook:

```bash
jupyter notebook
```

Kemudian buka:

```text
notebook.ipynb
```

Jalankan seluruh cell secara berurutan untuk melihat proses data understanding, data preparation, modeling, dan evaluation.

## Data Understanding

Tahap data understanding dilakukan untuk memahami struktur dan karakteristik dataset sebelum digunakan dalam proses pemodelan.

Beberapa pemeriksaan yang dilakukan meliputi:

- Ukuran dataset.
- Informasi tipe data.
- Daftar fitur.
- Missing value.
- Data duplikat.
- Statistik deskriptif.
- Distribusi target `Status`.

Dataset memiliki tiga kelas target, yaitu `Graduate`, `Dropout`, dan `Enrolled`.

Berdasarkan distribusi data, terdapat:

- 2.209 mahasiswa berstatus Graduate.
- 1.421 mahasiswa berstatus Dropout.
- 794 mahasiswa berstatus Enrolled.

Hal tersebut menunjukkan bahwa dropout merupakan permasalahan yang cukup signifikan karena mencakup sekitar sepertiga dari keseluruhan mahasiswa dalam dataset.

## Data Preparation

Pada tahap data preparation dilakukan beberapa proses untuk mempersiapkan data sebelum digunakan dalam pemodelan machine learning.

Tahapan yang dilakukan meliputi:

1. Memisahkan fitur dan target.
2. Mempertahankan target `Status` sebagai klasifikasi multiclass:
   - Graduate
   - Dropout
   - Enrolled
3. Mengidentifikasi fitur kategorikal dan numerik.
4. Membagi dataset menjadi:
   - 80% data training.
   - 20% data testing.
5. Menggunakan stratified splitting untuk menjaga proporsi setiap kelas.
6. Melakukan One-Hot Encoding pada fitur kategorikal.
7. Melakukan StandardScaler pada fitur numerik.
8. Menggabungkan preprocessing dan model menggunakan Scikit-learn Pipeline.

Pipeline digunakan agar preprocessing yang diterapkan ketika training tetap konsisten ketika model digunakan untuk melakukan prediksi terhadap data baru.

## Modeling

Pada tahap modeling digunakan tiga algoritma machine learning untuk dibandingkan, yaitu:

1. Logistic Regression
2. Random Forest Classifier
3. Gradient Boosting Classifier

Setiap model digabungkan dengan preprocessing menggunakan Pipeline.

Pendekatan ini membuat model dapat menerima data dengan struktur fitur asli dan secara otomatis melakukan preprocessing sebelum menghasilkan prediksi.

Model menghasilkan tiga kemungkinan status:

```text
Dropout
Enrolled
Graduate
```

Pemilihan model tidak hanya didasarkan pada accuracy, tetapi juga mempertimbangkan kemampuan model dalam mendeteksi mahasiswa yang benar-benar mengalami dropout.

## Evaluation

Evaluasi model dilakukan menggunakan beberapa metrik klasifikasi, yaitu:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- ROC-AUC

Selain performa keseluruhan model, perhatian khusus diberikan pada:

- Dropout Precision
- Dropout Recall
- Dropout F1-Score

Recall pada kelas `Dropout` menjadi salah satu metrik penting karena menunjukkan kemampuan model dalam mendeteksi mahasiswa yang benar-benar mengalami dropout.

Dalam konteks Jaya Jaya Institut, mahasiswa yang sebenarnya berisiko dropout tetapi tidak berhasil terdeteksi dapat kehilangan kesempatan untuk mendapatkan intervensi atau bimbingan lebih awal.

Model terbaik berdasarkan hasil evaluasi kemudian disimpan sebagai pipeline pada:

```text
model/student_status_model.pkl
```

Pipeline tersebut telah mencakup preprocessing dan model klasifikasi sehingga dapat digunakan langsung untuk melakukan prediksi terhadap data baru dengan struktur fitur yang sesuai.

## Menjalankan Sistem Machine Learning

Proyek ini menyediakan aplikasi prediksi berbasis Streamlit melalui file:

```text
app.py
```

Pastikan seluruh dependency sudah terinstal:

```bash
python -m pip install -r requirements.txt
```

Kemudian jalankan aplikasi:

```bash
python -m streamlit run app.py
```

Aplikasi biasanya dapat diakses melalui:

```text
http://localhost:8501
```

Melalui aplikasi tersebut, pengguna dapat memasukkan informasi mahasiswa dan memperoleh prediksi status:

- Dropout
- Enrolled
- Graduate

Aplikasi juga menampilkan probabilitas prediksi untuk masing-masing kelas.

Hasil prediksi dapat digunakan sebagai sistem pendukung keputusan untuk membantu institusi mengidentifikasi mahasiswa yang membutuhkan perhatian lebih lanjut.

> Hasil prediksi model sebaiknya digunakan sebagai alat bantu analisis dan bukan sebagai satu-satunya dasar dalam mengambil keputusan akademik terhadap mahasiswa.

## Business Dashboard

Business dashboard dibuat menggunakan **Metabase** untuk membantu pihak Jaya Jaya Institut memahami kondisi mahasiswa dan memonitor indikator yang berkaitan dengan dropout.

Dashboard menampilkan empat KPI utama:

- Total Students
- Total Dropout
- Dropout Rate
- Graduate Rate

Selain KPI, dashboard juga menampilkan beberapa visualisasi:

- Student Status Distribution
- Dropout Rate by Tuition Status
- Dropout Rate by Debtor Status
- Dropout Rate by Scholarship Status
- Dropout Rate by Age at Enrollment
- Dropout Rate by 1st Semester Performance
- Dropout Rate by Course

### Tampilan Dashboard

![Student Dropout Analysis Dashboard](maylatriana-dashboard.png)

### Hasil KPI Utama

Berdasarkan dashboard:

| KPI | Hasil |
|---|---:|
| Total Students | 4.424 |
| Total Dropout | 1.421 |
| Dropout Rate | 32,12% |
| Graduate Rate | 49,93% |

Hasil tersebut menunjukkan bahwa sekitar sepertiga mahasiswa dalam dataset memiliki status dropout sehingga permasalahan dropout perlu mendapatkan perhatian khusus dari institusi.

## Menjalankan Dashboard Metabase

Dashboard dibuat menggunakan Metabase dengan database aplikasi yang tersimpan pada:

```text
metabase.db.mv.db
```

Pada proses pengembangan proyek, data mahasiswa disimpan menggunakan PostgreSQL dan Metabase dijalankan menggunakan Docker.

Jika menggunakan konfigurasi Docker proyek, jalankan:

```bash
docker compose up -d
```

Setelah container aktif, dashboard dapat diakses melalui browser pada:

```text
http://localhost:3001
```

Database PostgreSQL yang digunakan pada konfigurasi proyek:

```text
Database : student_analytics
Username : student_user
Password : student123
Host     : postgres
Port     : 5432
```

Dataset utama tersimpan pada tabel:

```text
student_data
```

> Port PostgreSQL dari dalam jaringan Docker menggunakan port `5432`, sedangkan konfigurasi host dapat menggunakan port yang berbeda sesuai `docker-compose.yml`.

## Conclusion

Berdasarkan hasil analisis terhadap 4.424 data mahasiswa, ditemukan bahwa terdapat **1.421 mahasiswa berstatus dropout**, dengan tingkat dropout sebesar **32,12%**. Angka tersebut menunjukkan bahwa dropout merupakan permasalahan yang cukup signifikan bagi Jaya Jaya Institut.

Beberapa pola penting yang terlihat dari dashboard adalah sebagai berikut:

1. **Status pembayaran biaya pendidikan berkaitan kuat dengan dropout.**

   Mahasiswa dengan status pembayaran biaya pendidikan yang tidak up-to-date memiliki tingkat dropout yang jauh lebih tinggi dibandingkan mahasiswa yang pembayaran biaya pendidikannya lancar. Pada dashboard, kelompok dengan pembayaran tidak up-to-date memiliki dropout rate sekitar **86%**, sedangkan mahasiswa dengan pembayaran up-to-date memiliki tingkat dropout yang jauh lebih rendah.

2. **Mahasiswa dengan status debtor memiliki tingkat dropout lebih tinggi.**

   Kelompok mahasiswa dengan status debtor menunjukkan dropout rate sekitar **62%**, sedangkan mahasiswa non-debtor memiliki tingkat dropout yang lebih rendah. Hal ini menunjukkan bahwa kondisi finansial dapat menjadi salah satu indikator penting dalam monitoring risiko dropout.

3. **Penerima beasiswa memiliki tingkat dropout lebih rendah.**

   Mahasiswa yang menerima beasiswa memiliki dropout rate sekitar **12%**, sedangkan mahasiswa tanpa beasiswa memiliki tingkat dropout sekitar **39%**. Pola ini menunjukkan adanya hubungan antara dukungan finansial dan keberlanjutan studi mahasiswa.

4. **Usia saat pertama kali mendaftar menunjukkan perbedaan tingkat dropout.**

   Dashboard menunjukkan bahwa tingkat dropout berbeda antar kelompok usia. Kelompok mahasiswa yang masuk pada usia tertentu, terutama kelompok usia yang lebih tinggi dibanding mayoritas mahasiswa, menunjukkan tingkat dropout yang lebih besar dan dapat menjadi kelompok yang perlu diperhatikan lebih lanjut.

5. **Performa akademik semester pertama merupakan indikator penting.**

   Mahasiswa dengan jumlah mata kuliah yang berhasil diselesaikan sangat sedikit pada semester pertama menunjukkan tingkat dropout yang jauh lebih tinggi. Kelompok mahasiswa dengan **0 mata kuliah approved pada semester pertama memiliki dropout rate di atas 80%**.

   Sebaliknya, tingkat dropout cenderung menurun pada mahasiswa yang berhasil menyelesaikan lebih banyak mata kuliah pada semester pertama.

6. **Tingkat dropout berbeda antar course.**

   Dashboard menunjukkan adanya variasi dropout rate pada masing-masing course. Informasi ini dapat digunakan oleh institusi untuk melakukan analisis lebih lanjut terhadap program dengan tingkat dropout yang relatif tinggi.

Secara keseluruhan, hasil analisis menunjukkan bahwa faktor finansial dan performa akademik awal merupakan indikator penting yang dapat digunakan untuk membantu mendeteksi mahasiswa yang berpotensi mengalami dropout.

Model machine learning yang dibangun dalam proyek ini dapat digunakan sebagai alat bantu untuk memprediksi status mahasiswa sehingga institusi dapat melakukan monitoring dan intervensi secara lebih awal.

## Rekomendasi Action Items

Berdasarkan hasil analisis, beberapa rekomendasi yang dapat diterapkan oleh Jaya Jaya Institut adalah:

1. **Membuat sistem early warning untuk mahasiswa berisiko dropout.**

   Institusi dapat menggunakan hasil prediksi model machine learning sebagai salah satu indikator awal untuk mengidentifikasi mahasiswa yang memiliki risiko dropout. Mahasiswa dengan risiko tinggi dapat dimasukkan ke dalam daftar monitoring untuk dilakukan evaluasi lebih lanjut oleh pihak akademik.

2. **Melakukan monitoring pembayaran biaya pendidikan secara berkala.**

   Mahasiswa dengan status `Tuition Fees Up To Date = No` perlu mendapatkan perhatian lebih awal karena kelompok tersebut menunjukkan tingkat dropout yang sangat tinggi.

   Institusi dapat melakukan pendekatan kepada mahasiswa untuk mengetahui kendala pembayaran serta menawarkan solusi yang tersedia, seperti skema cicilan, bantuan finansial, atau informasi program bantuan pendidikan.

3. **Memberikan perhatian khusus kepada mahasiswa dengan status debtor.**

   Status debtor dapat digunakan sebagai salah satu indikator risiko finansial. Institusi dapat melakukan komunikasi lebih awal dengan mahasiswa yang memiliki kendala finansial sebelum masalah tersebut berdampak lebih jauh terhadap keberlanjutan studi.

4. **Memperkuat program beasiswa dan bantuan finansial.**

   Karena penerima beasiswa menunjukkan tingkat dropout yang lebih rendah, institusi dapat mengevaluasi kemungkinan perluasan program beasiswa atau bantuan pendidikan kepada mahasiswa yang memenuhi kriteria dan memiliki risiko finansial.

5. **Melakukan evaluasi akademik sejak semester pertama.**

   Jumlah mata kuliah yang berhasil diselesaikan pada semester pertama dapat digunakan sebagai indikator awal risiko dropout.

   Mahasiswa dengan jumlah mata kuliah approved yang sangat rendah dapat diberikan:
   - Bimbingan akademik.
   - Konsultasi dengan dosen pembimbing.
   - Program pendampingan belajar.
   - Evaluasi kesulitan akademik secara individual.

6. **Memberikan perhatian kepada kelompok usia dengan dropout rate tinggi.**

   Mahasiswa yang masuk pada usia lebih tinggi mungkin memiliki kebutuhan atau tantangan yang berbeda, seperti pekerjaan, keluarga, atau keterbatasan waktu.

   Institusi dapat mempertimbangkan dukungan yang lebih fleksibel sesuai kebutuhan mahasiswa, seperti konsultasi akademik atau pengaturan pembelajaran yang lebih adaptif.

7. **Melakukan evaluasi pada course dengan dropout rate tinggi.**

   Program studi atau course dengan tingkat dropout relatif tinggi perlu dianalisis lebih lanjut untuk mengetahui penyebabnya, seperti tingkat kesulitan akademik, kurikulum, beban studi, atau faktor lain yang memengaruhi keberlanjutan mahasiswa.

8. **Melakukan monitoring melalui dashboard secara berkala.**

   Dashboard dapat digunakan oleh pihak institusi untuk memonitor KPI utama seperti total mahasiswa, jumlah dropout, dropout rate, serta karakteristik kelompok mahasiswa dengan tingkat dropout tinggi.

   Monitoring secara berkala dapat membantu institusi melakukan tindakan berdasarkan data dan mengevaluasi efektivitas program intervensi yang telah dilakukan.

## Struktur Proyek

Struktur file submission:

```text
submission/
├── model/
│   └── student_status_model.pkl
├── notebook.ipynb
├── app.py
├── README.md
├── maylatriana-dashboard.png
├── metabase.db.mv.db
└── requirements.txt
```

Keterangan:

- `model/` : menyimpan model machine learning yang telah dilatih.
- `notebook.ipynb` : berisi proses data understanding, data preparation, modeling, dan evaluation.
- `app.py` : aplikasi Streamlit untuk melakukan prediksi status mahasiswa.
- `README.md` : dokumentasi proyek.
- `maylatriana-dashboard.png` : screenshot business dashboard.
- `metabase.db.mv.db` : database aplikasi Metabase yang menyimpan konfigurasi dashboard.
- `requirements.txt` : daftar library dan versi yang dibutuhkan untuk menjalankan proyek.

## Author

**Mayla Triana**

Proyek ini dibuat sebagai bagian dari submission akhir kelas Belajar Penerapan Data Science.