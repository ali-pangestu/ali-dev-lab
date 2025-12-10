print("--- DAY 11: LATIHAN LOGIKA & KOMPARASI ---")

# Kasus: Kita ingin mengecek apakah angka input user
# berada di rentang lebih dari 3 DAN kurang dari 10.

input_user = 7 # Coba ganti angka ini nanti (misal: 1, 7, atau 12)

# 1. Cek apakah lebih dari 3?
lebih_dari_3 = input_user > 3
print(f"Lebih dari 3? {lebih_dari_3}")

# 2. Cek apakah kurang dari 10?
kurang_dari_10 = input_user < 10
print(f"Kurang dari 10? {kurang_dari_10}")

# 3. GABUNGKAN DENGAN 'AND'
# Angka benar JIKA (lebih dari 3) DAN (kurang dari 10)
is_correct = lebih_dari_3 and kurang_dari_10

print(f"Angka yang dimasukkan: {input_user}")
print(f"Apakah angka valid (antara 3 - 10)? -> {is_correct}")

# Tips Pro: Di Python bisa ditulis: 3 < input_user < 10
# Tapi untuk belajar logika, kita pakai cara 'and' dulu ya.