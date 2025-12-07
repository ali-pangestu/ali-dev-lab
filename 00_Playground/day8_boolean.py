print("--- DAY 8: TIPE DATA BOOLEAN ---")
# Boolean cuma punya 2 nilai: True atau False
# Perhatikan: Huruf depan harus KAPITAL (T/F)

saya_manusia = True
saya_robot = False

print("Apakah saya manusia?", saya_manusia)
print("Apakah saya robot?", saya_robot)

print("\n--- KONSEP 0 dan 1 ---")
# Di komputer, True itu 1, False itu 0.
x = 10
y = 0

print(f"Angka {x} dianggap True/False? -> {bool(x)}")
print(f"Angka {y} dianggap True/False? -> {bool(y)}")

# Tips Penting:
# Angka 0 = False
# Angka selain 0 (mau 1, 100, -5) = True
# String kosong "" = False
# String ada isinya "Halo" = True

print("\n--- CEK STRING KOSONG ---")
nama_user = "Sayang"
nama_kosong = ""

print(f"Variabel 'nama_user' isinya ada? -> {bool(nama_user)}")
print(f"Variabel 'nama_kosong' isinya ada? -> {bool(nama_kosong)}")