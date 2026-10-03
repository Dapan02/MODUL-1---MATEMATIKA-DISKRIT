pakai_fingerprint = True
pakai_pin_pad = True

# Model logika
akses_diterima = pakai_fingerprint ^ pakai_pin_pad 

if akses_diterima:
 print("akses DITERIMA (pintu berhasil dibuka)")
else:
 print("akses DITOLAK (gagal verifikasi)")