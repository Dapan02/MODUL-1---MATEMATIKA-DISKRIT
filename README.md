# MODUL-1-MATEMATIKA-DISKRIT
Laporan praktikum modul satu Matematika Diskrit 

• NAMA : Muhammad Dafan Arsenal Ramadhan 

• KELAS : 1B

• NIM : 260306074

# MAKSUD DAN TUJUAN REPOSITORY
### Maksud
Repository ini dibuat untuk mendokumentasikan hasil Laporan Praktikum (Laprak) Modul 1 Mata Kuliah Matematika Diskrit / Logika Pemrograman. Repository ini berisi implementasi program berbasis bahasa Python yang mensimulasikan berbagai studi kasus pengambilan keputusan menggunakan logika Boolean (*AND*, *OR*, dan *XOR*), dilengkapi dengan evaluasi tabel kebenaran (*truth table*) serta pengujian sistem.

### Tujuan
1. **Memahami Konsep Logika Dasar:** Mempelajari dan menerapkan operasi logika Boolean (*AND*, *OR*, *XOR*) dalam menyelesaikan permasalahan akademis maupun kasus nyata.
2. **Implementasi ke Pemrograman Python:** Mengubah kondisi dan aturan keputusan dari studi kasus nyata menjadi kode program Python yang efisien dan presisi.
3. **Pembuktian Kebenaran Logika:** Menyusun dan memverifikasi tabel kebenaran (*truth table*) untuk setiap kombinasi nilai *input* guna memastikan alur logika program sesuai dengan aturan yang ditetapkan.
4. **Pengujian Sistem (Software Testing):** Melakukan pengujian terhadap seluruh studi kasus program untuk memastikan output sistem valid dan mendapatkan status pengujian **PASS**.
5. **Dokumentasi Praktikum:** Menyediakan rekam jejak pengerjaan tugas praktikum yang rapi, terstruktur, dan mudah diakses sebagai bahan evaluasi dan pembelajaran.
   
# STUDI KASUS
1. penerima beasiswa mahasiswa
2. Siswa naik kelas
3. Seleksi siswa
4. Rekrutmen pekerja
5. verifikasi mahasiswa
6. Kredit bank
7. Akses wahana roller coaster
8. Akses membuka pintu

# ALUR MATERI
alur pembelajaran pada praktikum Modul 1 ini dibagi menjadi beberapa tahapan:

1. Perkenalan Tipe Data Boolean & Variabel Kondisi
* **Apa itu Boolean?** Mengenal tipe data dasar yang hanya punya dua nilai: `True` (T / Benar) dan `False` (F / Salah).
* **Menentukan Variabel:** Belajar mengubah syarat dunia nyata menjadi variabel logika. 
  * *Contoh:* Syarat naik roller coaster diubah jadi variabel `tinggi_badan_cukup` dan `umur_cukup`.

2. Memahami Operator Logika Dasar
Mempelajari cara menggabungkan beberapa kondisi menggunakan 3 gerbang logika utama:
* **Logika AND (`and`):** Sifatnya "ketat". Hasilnya baru `True` kalau **semua** syarat bernilai `True`.
* **Logika OR (`or`):** Sifatnya "fleksibel". Hasilnya jadi `True` selama ada **minimal satu** syarat yang bernilai `True`.
* **Logika XOR (`^` / Exclusive OR):** Sifatnya "pilih salah satu". Hasilnya `True` hanya kalau nilai kondisinya **berbeda** (satu `True` dan satu `False`).

3. Pembuatan Tabel Kebenaran (Truth Table)
* Menentukan hasil akhir (*output*) secara manual berdasarkan aturan logika yang digunakan sebelum dituangkan ke kode program.

4. Implementasi Kode Program di Python
* Mengubah model logika yang sudah dirancang ke dalam sintaks Python.
* Menggunakan struktur percabangan (`if - else`) untuk menentukan keputusan/output berdasarkan nilai variabel.

5. Pengujian Sistem (System Testing) & Dokumentasi
* **Uji Coba Kode:** Menjalankan program menggunakan berbagai kombinasi variabel untuk memastikan hasilnya cocok dengan Tabel Kebenaran.
* **Penentuan Status:** Menandai hasil pengujian dengan status **PASS** jika output program sudah 100% sesuai dengan logika.
* **Upload ke GitHub:** Merapikan struktur folder dan mendokumentasikan seluruh materi ke dalam repository GitHub.
  
# MENJALANKAN PROGRAM
# Panduan Instalasi dan Menjalankan Python via CMD

## 1. Unduh dan Instal Python
* Buka peramban (*browser*) dan kunjungi situs resmi [python.org/downloads](https://www.python.org/downloads/).
* Unduh berkas *installer* Python versi terbaru untuk Windows.
* Jalankan berkas *installer* yang telah diunduh.
* **Sangat Penting:** Centang opsi **"Add python.exe to PATH"** di bagian bawah jendela instalasi sebelum menekan **Install Now**.

## 2. Cek Instalasi Python melalui CMD
* Tekan kombinasi tombol **Win + R** pada papan ketik, ketik `cmd`, lalu tekan **Enter**.
* Di dalam jendela CMD, ketik `python --version` lalu tekan **Enter**.
* Jika berhasil, CMD akan menampilkan versi Python yang terpasang (contoh: `Python 3.12.x`). Jika muncul pesan eror/tidak ditemukan, pastikan proses instalasi pada langkah pertama sudah benar.

## 3. Membuat dan Membuka File di Notepad
* Di dalam CMD, ketik `notepad contoh.py` lalu tekan **Enter**.
* Jika muncul jendela pop-up konfirmasi untuk membuat berkas baru, pilih **Yes**.

## 4. Menginput dan Menyimpan Kode
* Salin (*copy*) kode program Python yang telah Anda siapkan.
* Tempel (*paste*) kode tersebut ke dalam jendela Notepad yang terbuka (`Ctrl + V`).
* Simpan perubahan dengan menekan **Ctrl + S**, lalu tutup jendela Notepad.

## 5. Menjalankan Kode Python
* Kembali ke jendela CMD.
* Ketik `python contoh.py` lalu tekan **Enter** untuk mengeksekusi dan menampilkan hasil dari kode program Anda.
  
