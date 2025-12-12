print("--- DAY 13: PENGENALAN STRING (TEKS) ---")

# 1. Cara Standar (Kutip Dua & Kutip Satu)
# Dua-duanya boleh dipakai di Python
nama = "Sayang"
hobi = 'Coding'
print(f"Halo {nama}, yuk {hobi}!")

# 2. Hati-hati dengan Tanda Kutip di dalam kalimat!
# Salah: hari = 'Jum'at'  <- Error, karena dikira stringnya cuma 'Jum'

# Solusi A: Pakai kutip dua di luar
hari = "Hari Jum'at" 
print(hari)

# Solusi B: Pakai tanda 'Backslash' (\) biar kutipnya dianggap teks biasa
kalimat = 'Dia bilang: "Aku mau coding besok"'
kalimat_ribet = 'Ini hari Jum\'at' # Tanda \ bikin ' setelahnya jadi teks biasa
print(kalimat)
print(kalimat_ribet)

# 3. String Multiline (Paragraf)
# Pakai kutip tiga (""" atau ''')
pantun = """
Jalan-jalan ke kota Paris,
Lihat gedung berbaris-baris.
Walau coding sampai nangis,
Hasilnya pasti manis.
"""
print(pantun)