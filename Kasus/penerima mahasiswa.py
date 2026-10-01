aktif_kuliah = True
nilai_memenuhi = True
bebas_sanksi = True

# Model logika
diterima = aktif_kuliah and nilai_memenuhi and bebas_sanksi

if diterima:
	print("Mahasiswa DITERIMA beasiswa")
else:
	print("Mahasiswa TIDAK DITERIMA beasiswa")
