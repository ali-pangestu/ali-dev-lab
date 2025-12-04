print("--- LATIHAN DAY 5: F-STRING (FORMATTING) ---")

# 1. SIAPKAN DATA
nama_mata_uang = "Won Korea (KRW)"
kurs_tukar = 12 # Anggap 1 Won = 12 Rupiah (kurang lebih)
target_uang_won = 5000 # Mau bawa 5000 Won buat jajan odeng

# 2. HITUNG MATEMATIKA (Operasi Aritmatika)
# Kita hitung berapa Rupiah yang harus disiapkan
butuh_rupiah = target_uang_won * kurs_tukar

# 3. TAMPILKAN DENGAN CANTIK (Pakai f-string)
# Perhatikan huruf 'f' kecil sebelum tanda kutip pembuka!
# Di dalam kurung kurawal {}, kita bisa taruh variabel
print(f"Halo Ali! Kamu mau tukar {target_uang_won} {nama_mata_uang}.")
print(f"Kurs hari ini: 1 Won = {kurs_tukar} Rupiah.")
print(f"Jadi, kamu harus siapkan: Rp {butuh_rupiah} cash.")

# Cobain: Kalau huruf 'f' nya dihapus, apa yang terjadi? (Pasti berantakan/error)