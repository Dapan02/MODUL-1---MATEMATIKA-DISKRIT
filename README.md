# MODUL-1---MATEMATIKA-DISKRIT
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
1. Verifikasi mahasiswa
2. Siswa naik kelas
3. Seleksi siswa
4. Rekrutmen pekerja
5. Penerima mahasiswa
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
1. Cari/search di Windows, lalu ketik "cmd" lalu "Enter" atau gampangnya bisa dengan "Ctrl + R" dan tekan "Enter"
2. Di dalam cmd ketik "python --version" (opsional) untuk memastikan python sudah ter-install di laptop atau tidak (jika python ada dilayar cmd akan memunculkan versi python yang digunakan, jika tidak biasanya akan bertulis "can't found" yang tandanya pengguna harus mendownload python terlebih dahulu)
3. Setelah mengetahui python sudah ter-install, ketik "notepad contoh.py" di CMD lalu tekan enter, jika muncul pop-up untuk membuat file baru, klik yes dan tempatkan file tersebut di folder yang sudah disediakan
4. Dalam notepad masukan kode yang ingin dimasukkan (ctrl + c), lalu tempel (paste) ke dalam notepad (ctrl + v)
