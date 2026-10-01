Pendidikan_sesuai = True
lulus_tes = True
usia_memenuhi = False

# Model logika
diterima_bekerja = Pendidikan_sesuai and lulus_tes and usia_memenuhi

if diterima_bekerja:
	print("kandidat DITERIMA untuk bekerja")
else:
	print("kandidat TIDAK DITERIMA untuk bekerja")
