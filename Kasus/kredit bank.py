ada_agunan_tambahan = True
ada_penjamin = True
nasabah_prioritas = True

# Model logika
lulus_proses_khusus = ada_agunan_tambahan or ada_penjamin or nasabah_prioritas

if lulus_proses_khusus:
	print("pengajuan kredit DISETUJUI pihak bank")
else:
	print("pengajuan kredit TIDAK DISETUJUI pihak bank")
