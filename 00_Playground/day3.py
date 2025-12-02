print("--- LATIHAN DAY 3: TIPE DATA ---")

# 1. PERCOBAAN: TEKS vs ANGKA
# Pakai tanda kutip "" artinya TEKS (String)
print("10" + "10")  
# Hasilnya bakal "1010" (Digabung kayak kereta)

# Tanpa tanda kutip artinya ANGKA (Integer)
print(10 + 10)      
# Hasilnya bakal 20 (Dihitung matematika)

# 2. PERCOBAAN: CEK KTP (Mengecek Tipe Data)
nama = "Ali"
berat = 48
tinggi = 168.5 # Pakai titik, bukan koma (Float/Desimal)

print("\n--- CEK IDENTITAS VARIABEL ---")
print(type(nama))   # Harus keluar <class 'str'> (String)
print(type(berat))  # Harus keluar <class 'int'> (Integer)
print(type(tinggi)) # Harus keluar <class 'float'> (Desimal)