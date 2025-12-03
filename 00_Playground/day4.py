print("--- LATIHAN DAY 4: MESIN YANG BISA NGOBROL ---")

# 1. INPUT: Komputer bertanya, lalu menunggu kamu mengetik jawaban
# Perintah input() akan membuat kursor berkedip di Terminal bawah
nama = input("Halo! Siapa nama kamu? ")

# 2. INPUT LAGI: Tanya target tabungan
# Apapun yang kamu ketik di sini akan dianggap TEKS (String) oleh Python
target_tabungan = input("Mau nabung berapa juta buat ke Korea? ")

# 3. OUTPUT: Komputer merespons jawabanmu
# Kita pakai f-string (huruf f di depan tanda kutip) biar gampang nyelipin variabel
print(f"Oke {nama}, semangat ya! Target {target_tabungan} juta pasti tercapai.")
print("Sampai ketemu di Seoul! 🇰🇷")