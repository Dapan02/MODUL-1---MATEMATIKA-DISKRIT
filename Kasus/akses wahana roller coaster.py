tinggi_badan_cukup = True
umur_cukup = True

# Model logika
bisa_naik_wahana = tinggi_badan_cukup ^ umur_cukup 

if bisa_naik_wahana:
 print("DIPERBOLEHKAN naik wahana roller coaster")
else:
 print("TIDAK DIPERBOLEHKAN naik wahana roller coaster")
