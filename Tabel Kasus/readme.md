# Tabel Kebenaran (Truth Table) Modul 1

## KELOMPOK 1: LOGIKA AND (and)
Aturan: Hasil TRUE hanya jika SEMUA syarat bernilai T.

### 1. Penerima Beasiswa (penerima mahasiswa.py)
| Aktif Kuliah | Nilai Cukup | Bebas Sanksi | Hasil |
| :---: | :---: | :---: | :---: |
| T | T | T | T |
| T | T | F | F |
| T | F | T | F |
| T | F | F | F |
| F | T | T | F |
| F | T | F | F |
| F | F | T | F |
| F | F | F | F |

### 2. Rekrutmen Pekerja (rekruitmen pekerja.py)
| Pendidikan Sesuai | Lulus Tes | Usia Cukup | Hasil |
| :---: | :---: | :---: | :---: |
| T | T | T | T |
| T | T | F | F |
| T | F | T | F |
| T | F | F | F |
| F | T | T | F |
| F | T | F | F |
| F | F | T | F |
| F | F | F | F |

### 3. Seleksi Siswa (seleksi siswa.py)
| Aktif | Nilai Cukup | Prasyarat | Hasil |
| :---: | :---: | :---: | :---: |
| T | T | T | T |
| T | T | F | F |
| T | F | T | F |
| T | F | F | F |
| F | T | T | F |
| F | T | F | F |
| F | F | T | F |
| F | F | F | F |

---

## KELOMPOK 2: LOGIKA OR (or)
Aturan: Hasil TRUE jika MINIMAL SALAH SATU syarat bernilai T.

### 4. Verifikasi Mahasiswa (verifikasi mahasiswa.py)
| Punya NIM | Bawa KTP | Email Kampus | Hasil |
| :---: | :---: | :---: | :---: |
| T | T | T | T |
| T | T | F | T |
| T | F | T | T |
| T | F | F | T |
| F | T | T | T |
| F | T | F | T |
| F | F | T | T |
| F | F | F | F |

### 5. Siswa Naik Kelas (siswa naik kelas.py)
| Rata-rata Cukup | Lulus Remedial | Keaktifan | Hasil |
| :---: | :---: | :---: | :---: |
| T | T | T | T |
| T | T | F | T |
| T | F | T | T |
| T | F | F | T |
| F | T | T | T |
| F | T | F | T |
| F | F | T | T |
| F | F | F | F |

### 6. Kredit Bank (kredit bank.py)
| Agunan | Penjamin | Prioritas | Hasil |
| :---: | :---: | :---: | :---: |
| T | T | T | T |
| T | T | F | T |
| T | F | T | T |
| T | F | F | T |
| F | T | T | T |
| F | T | F | T |
| F | F | T | T |
| F | F | F | F |

---

## KELOMPOK 3: LOGIKA XOR (^)
Aturan: Hasil TRUE hanya jika nilainya BERBEDA (satu T dan satu F).

### 7. Akses Roller Coaster (akses wahana roller coaster.py)
| Tinggi Cukup | Umur Cukup | Hasil |
| :---: | :---: | :---: |
| T | T | F |
| T | F | T |
| F | T | T |
| F | F | F |

### 8. Akses Membuka Pintu (akses membuka pintu.py)
| Fingerprint | PIN Pad | Hasil |
| :---: | :---: | :---: |
| T | T | F |
| T | F | T |
| F | T | T |
| F | F | F |
