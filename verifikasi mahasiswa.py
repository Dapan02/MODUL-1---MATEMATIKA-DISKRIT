punya_nim = True
membawa_ktp = True
login_email_kampus = True

# Model logika
terverifikasi_mahasiswa = punya_nim or membawa_ktp or login_email_kampus

if terverifikasi_mahasiswa:
 print("verifikasi BERHASIL, anda berstatus mahasiswa")
else:
 print("verifikasi GAGAL, anda belum berstatus mahasiswa")