print("--- DAY 14: OPERASI STRING (SAMBUNG & CEK) ---")

nama_depan = "Coding"
nama_belakang = "Everyday"

# 1. Menyambung String (Concatenation)
# Pakai tanda tambah (+)
nama_lengkap = nama_depan + " " + nama_belakang
print(f"Gabungan: {nama_lengkap}")

# 2. Menghitung Panjang String
# Pakai fungsi len() -> length
panjang = len(nama_lengkap)
print(f"Panjang huruf (termasuk spasi): {panjang}")

# 3. Operator Cek (in)
# Mengecek apakah ada huruf/kata tertentu
cek_huruf = "d"
status = cek_huruf in nama_lengkap
print(f"Apakah ada huruf '{cek_huruf}' di '{nama_lengkap}'? -> {status}")

# 4. Mengulang String
# Pakai tanda kali (*)
ketawa = "wk" * 5
print(f"Ketawa online: {ketawa}")

# 5. Indexing (Mengambil huruf ke-n)
# Ingat: Python mulai hitung dari 0!
huruf_pertama = nama_lengkap[0] # Ambil huruf C
huruf_keenam = nama_lengkap[6]  # Ambil spasi (karena C-o-d-i-n-g itu 0-1-2-3-4-5)
print(f"Huruf pertama: {huruf_pertama}")
print(f"Huruf index ke-6: '{huruf_keenam}'")