print("--- PROJECT DAY 6: KALKULATOR BMI ---")
print("Aplikasi pengecek status berat badan\n")

# 1. INPUT DATA (Penting: Pakai float() biar bisa desimal/koma)
# Kalau cuma input(), Python anggap itu Teks. Gak bisa dikali/bagi.
# Jadi kita bungkus pakai float(...) biar jadi angka.
nama = input("Siapa nama kamu? ")
berat = float(input("Masukkan berat badan (kg): "))
tinggi_cm = float(input("Masukkan tinggi badan (cm): "))

# 2. KONVERSI & HITUNG (Logika Matematika)
# Rumus BMI butuh tinggi dalam Meter, bukan CM.
tinggi_m = tinggi_cm / 100 

# Rumus BMI: Berat / (Tinggi x Tinggi)
bmi = berat / (tinggi_m * tinggi_m)

# 3. TAMPILKAN HASIL (f-string)
# Tips: {bmi:.2f} artinya ambil 2 angka saja di belakang koma biar rapi.
print("-------------------------------")
print(f"Halo {nama}, hasil diagnosa kamu:")
print(f"Berat: {berat} kg")
print(f"Tinggi: {tinggi_m} m")
print(f"Skor BMI kamu: {bmi:.2f}")
print("-------------------------------")
print("Target kita: BMI 22 (Athletic Body). Semangat makan protein! 💪")