# TESTING-PENGUJIAN SISTEMATIS Modul 1

## KELOMPOK 1: LOGIKA AND (and)
Aturan: Hasil TRUE hanya jika SEMUA syarat bernilai T.

### 1. Penerima Beasiswa (penerima mahasiswa.py)
| Aktif Kuliah | Nilai Cukup | Bebas Sanksi | Hasil | Status Test |
| :---: | :---: | :---: | :---: | :---: |
| T | T | T | T | PASS |
| T | T | F | F | PASS |
| T | F | T | F | PASS |
| T | F | F | F | PASS |
| F | T | T | F | PASS |
| F | T | F | F | PASS |
| F | F | T | F | PASS |
| F | F | F | F | PASS |

### 2. Rekrutmen Pekerja (rekruitmen pekerja.py)
| Pendidikan Sesuai | Lulus Tes | Usia Cukup | Hasil | Status Test |
| :---: | :---: | :---: | :---: | :---: |
| T | T | T | T | PASS |
| T | T | F | F | PASS |
| T | F | T | F | PASS |
| T | F | F | F | PASS |
| F | T | T | F | PASS |
| F | T | F | F | PASS |
| F | F | T | F | PASS |
| F | F | F | F | PASS |

### 3. Seleksi Siswa (seleksi siswa.py)
| Aktif | Nilai Cukup | Prasyarat | Hasil | Status Test |
| :---: | :---: | :---: | :---: | :---: |
| T | T | T | T | PASS |
| T | T | F | F | PASS |
| T | F | T | F | PASS |
| T | F | F | F | PASS |
| F | T | T | F | PASS |
| F | T | F | F | PASS |
| F | F | T | F | PASS |
| F | F | F | F | PASS |

---

## KELOMPOK 2: LOGIKA OR (or)
Aturan: Hasil TRUE jika MINIMAL SALAH SATU syarat bernilai T.

### 4. Verifikasi Mahasiswa (verifikasi mahasiswa.py)
| Punya NIM | Bawa KTP | Email Kampus | Hasil | Status Test |
| :---: | :---: | :---: | :---: | :---: |
| T | T | T | T | PASS |
| T | T | F | T | PASS |
| T | F | T | T | PASS |
| T | F | F | T | PASS |
| F | T | T | T | PASS |
| F | T | F | T | PASS |
| F | F | T | T | PASS |
| F | F | F | F | PASS |

### 5. Siswa Naik Kelas (siswa naik kelas.py)
| Rata-rata Cukup | Lulus Remedial | Keaktifan | Hasil | Status Test |
| :---: | :---: | :---: | :---: | :---: |
| T | T | T | T | PASS |
| T | T | F | T | PASS |
| T | F | T | T | PASS |
| T | F | F | T | PASS |
| F | T | T | T | PASS |
| F | T | F | T | PASS |
| F | F | T | T | PASS |
| F | F | F | F | PASS |

### 6. Kredit Bank (kredit bank.py)
| Agunan | Penjamin | Prioritas | Hasil | Status Test |
| :---: | :---: | :---: | :---: | :---: |
| T | T | T | T | PASS |
| T | T | F | T | PASS |
| T | F | T | T | PASS |
| T | F | F | T | PASS |
| F | T | T | T | PASS |
| F | T | F | T | PASS |
| F | F | T | T | PASS |
| F | F | F | F | PASS |

---

## KELOMPOK 3: LOGIKA XOR (^)
Aturan: Hasil TRUE hanya jika nilainya BERBEDA (satu T dan satu F).

### 7. Akses Roller Coaster (akses wahana roller coaster.py)
| Tinggi Cukup | Umur Cukup | Hasil | Status Test |
| :---: | :---: | :---: | :---: |
| T | T | F | PASS |
| T | F | T | PASS |
| F | T | T | PASS |
| F | F | F | PASS |

### 8. Akses Membuka Pintu (akses membuka pintu.py)
| Fingerprint | PIN Pad | Hasil | Status Test |
| :---: | :---: | :---: | :---: |
| T | T | F | PASS |
| T | F | T | PASS |
| F | T | T | PASS |
| F | F | F | PASS |
