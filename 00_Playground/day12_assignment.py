print("--- DAY 12: OPERATOR ASSIGNMENT (PENYINGKATAN) ---")

# 1. Penjumlahan (+=)
a = 10
print(f"Nilai a awal = {a}")

a += 5  # Ini artinya sama dengan: a = a + 5
print(f"Nilai a setelah (+= 5) = {a}") 

# 2. Pengurangan (-=)
b = 100
print(f"\nNilai b awal = {b}")

b -= 10 # Sama dengan: b = b - 10
print(f"Nilai b setelah (-= 10) = {b}")

# 3. Perkalian (*=)
c = 5
print(f"\nNilai c awal = {c}")

c *= 2 # Sama dengan: c = c * 2
print(f"Nilai c setelah (*= 2) = {c}")

# 4. Pembagian (/=)
d = 50
print(f"\nNilai d awal = {d}")

d /= 5 # Sama dengan: d = d / 5
print(f"Nilai d setelah (/= 5) = {d}")

# Challenge kecil:
# Ini sering dipakai buat "Skor Game". 
# Kalau menang, skor nambah.
skor = 0
skor += 100 # Menang ronde 1
skor += 50  # Bonus
print(f"\nSkor Akhir: {skor}")