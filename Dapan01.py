aktif = True
nilai_memenuhi = False
prasyarat = True

# Model logika
lulus = aktif and nilai_memenuhi and prasyarat
# Output hasil seleks	
if lulus:
	print("Peserta LULUS seleksi")
else:
	print("Peserta TIDAK LULUS seleksi")
