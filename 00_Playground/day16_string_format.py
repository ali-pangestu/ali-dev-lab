print("--- DAY 16: STRING FORMATTING (RATA KANAN KIRI) ---")

# Contoh: Mau bikin struk belanja
barang = "Kopi"
harga = 25000

# Cara Biasa (Jelek kalau beda panjang)
print("Barang:", barang)
print("Harga:", harga)

print("\n--- VERSI RAPI (F-STRING) ---")
# < : Rata Kiri
# > : Rata Kanan
# ^ : Rata Tengah
# Angka (10, 20) : Jatah lebar spasi

print(f"| {barang:<10} | {harga:>10} |") 
print(f"| {'Gula':<10} | {15000:>10} |") 
print(f"| {'Total':<10} | {40000:>10} |")

# Tips: Perhatikan outputnya di terminal, jadi lurus kan ya?