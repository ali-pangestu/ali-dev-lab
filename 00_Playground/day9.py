print("--- DAY 9: OPERASI KOMPARASI ---")
# Kita akan mengadu dua buah nilai
a = 10
b = 5

print(f"Nilai a = {a}, Nilai b = {b}")

# 1. LEBIH BESAR DARI (>)
print("Apakah a > b?", a > b) # Harusnya True

# 2. LEBIH KECIL DARI (<)
print("Apakah a < b?", a < b) # Harusnya False

# 3. SAMA DENGAN (==) -> Perhatikan: sama dengannya ada DUA
print("Apakah a == b?", a == b) 

# 4. TIDAK SAMA DENGAN (!=) -> Tanda seru artinya 'TIDAK'
print("Apakah a != b?", a != b)

# 5. LEBIH BESAR/KECIL SAMA DENGAN (>=, <=)
c = 10
print(f"\nNilai c = {c}")
print("Apakah a >= c?", a >= c) # True karena 10 sama dengan 10

print("\n--- CONTOH REAL CASE ---")
# Bayangkan aplikasi cek umur
umur_kamu = 25
syarat_umur_kerja = 18

boleh_kerja = umur_kamu >= syarat_umur_kerja
print(f"Umur {umur_kamu}, syarat {syarat_umur_kerja}. Boleh kerja? {boleh_kerja}")