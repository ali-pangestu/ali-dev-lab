print("--- DAY 15: STRING METHODS (GAYA HURUF) ---")

judul = "belajar python itu seru"
alay = "HaLo ApA KaBaR"
berantakan = "   Spasi Kiri Kanan Banyak   "

# 1. Mengubah Case (Huruf Besar/Kecil)
print(f"Normal: {judul}")
print(f"Upper (Kapital semua): {judul.upper()}")
print(f"Capitalize (Huruf awal doang): {judul.capitalize()}")
print(f"Title (Tiap kata): {judul.title()}")

# 2. Memperbaiki Huruf (Normalisasi)
# Berguna kalau user nulisnya gede kecil gak jelas
print(f"\nAlay: {alay}")
print(f"Dibenerin (Lower): {alay.lower()}")

# 3. Membersihkan Spasi (Strip)
# Berguna banget pas user input password/username ada spasi gak sengaja
print(f"\nAsli: '{berantakan}'")
print(f"Strip (Hapus spasi ujung): '{berantakan.strip()}'")

# 4. Mengganti Kata (Replace)
kalimat_salah = "Aku suka makan batu"
kalimat_benar = kalimat_salah.replace("batu", "bakso")
print(f"\nSalah: {kalimat_salah}")
print(f"Benar: {kalimat_benar}")