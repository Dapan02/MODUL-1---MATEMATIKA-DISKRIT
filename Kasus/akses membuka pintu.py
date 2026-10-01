pakai_fingerprint = True
pakai_pin_pad = True
pakai_kartu_akses = False

# Model logika
akses_diterima = pakai_fingerprint ^ pakai_pin_pad ^ pakai_kartu_akses

if akses_diterima:
 print("akses DITERIMA (pintu berhasil dibuka)")
else:
 print("akses DITOLAK (gagal verifikasi)")