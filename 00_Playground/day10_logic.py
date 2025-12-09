print("--- DAY 10: OPERASI LOGIKA BOLEAN ---")

# Data awal
punya_tiket = True
punya_ktp = False

print(f"Punya Tiket = {punya_tiket}")
print(f"Punya KTP = {punya_ktp}")

print("\n--- 1. LOGIKA AND (Dua-duanya harus True) ---")
# Bayangkan masuk konser: Harus bawa tiket DAN KTP
bisa_masuk = punya_tiket and punya_ktp
print(f"Apakah bisa masuk (Tiket AND KTP)? -> {bisa_masuk}") 
# Hasil: False (karena gak punya KTP)

print("\n--- 2. LOGIKA OR (Salah satu aja cukup) ---")
# Bayangkan diskon: Member ATAU Belanja > 100rb
is_member = False
belanja_banyak = True
dapat_diskon = is_member or belanja_banyak
print(f"Apakah dapat diskon (Member OR Belanja Banyak)? -> {dapat_diskon}")
# Hasil: True (karena belanja banyak bernilai True)

print("\n--- 3. LOGIKA NOT (Kebalikan) ---")
kany_ngantuk = True
# Kalau NOT ngantuk, berarti segar
print(f"Status Kany: Ngantuk? {kany_ngantuk}")
print(f"Apakah Kany segar (NOT ngantuk)? {not kany_ngantuk}")

print("\n--- CONTOH GABUNGAN (GABUNGAN COMPARISON) ---")
# Syarat kerja: Umur > 18 DAN Lulus Ujian
umur = 20
lulus = True

hasil_seleksi = (umur > 18) and lulus
print(f"Pelamar umur {umur} & status lulus {lulus}. Diterima? {hasil_seleksi}")