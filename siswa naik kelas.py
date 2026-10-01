nilai_rata_rata_cukup = True
Lulus_ujian_remedial = True
keaktifan_siswa = True

# Model logika
bisa_naik_kelas = nilai_rata_rata_cukup or Lulus_ujian_remedial or Keaktifan_siswa

if bisa_naik_kelas:
 print("siswa NAIK KELAS")
else:
 print("siswa TIDAK NAIK KELAS")
