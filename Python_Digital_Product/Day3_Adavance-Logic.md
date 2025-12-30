# ADVANCE LOGIC (Membuat Program Cerdas)

Ini bab lanjutan untuk logika yang lebih kompleks (multiple choice & syarat berlapis).

**Materi Utama** :

* `elif` **(Else If)** : Jembatan ketika pilihan tidak cuma dua. (Cek syarat A, kalau gagal cek syarat B, kalau gagal baru ke `else`).
* `and` : Dua syarat **wajib** benar (Strict).
* `or` : Salah satu benar, boleh masuk (Flexible).
* `not` : Membalikkan logika (True jadi False).
* **Nested IF** (bersarang) : Menaruh `if` di dalam `if`. Seperti membuka kotak di dalam kotak.


1. **Mengenal `elif` (Pilihan Lebih dari Dua)**
   
   Dunia tidak selalu hitam dan putih (Ya/Tidak). Kadang ada pilihan ketiga. `elif` (singkatan dari *Else If*) digunakan untuk mengecek kondisi lain jika kondisi pertama gagal.

2. **Operator Logika : Si Penentu Syarat**
   
   Kadang satu syarat aja ga cukup. Kita butuh 'operator' untuk menggabungkan syarat-syarat tersebut :
   
* `and` (dan): Semua syarat **wajib** terpenuhi. 
  *Analogi*: Kamu bisa ke Korea jika: Punya Paspor **AND** Punya Visa. (Kurang satu saja, tidak bisa berangkat).
   
* `or` (atau): Salah saru syarat terpenuhi sudah cukup.
  *Analogi*: Kamu bisa bayar pakai: Uang Tunai **OR** Kartu Kredit. (Pilih salah satu, tetap bisa transaksi).
   
* `not` (bukan/tidak): Digunakan untuk membalikkan keadaan. 
  *Analogi*: Jika **NOT** hujan, maka kita pergi.

3. **Nested IF (Logika Bersarang)**
   
Ini adalah teknik menaruh `if` di dalam `if`. Gunanya untuk pengecekan yang lebih *mendalam*.
   * *Contoh*: 1. Cek dulu: Apakah sudah login? (Jika iya, lanjut ke dalam). 2. Cek lagi: Apakah dia admin? (Jika iya, berikan akses penuh).


## PRAKTEK KODE

```python
# Skenario: Cek Kesiapan Pulang Kampung & Korea
tabungan_juta = 210
berat_badan = 66
lokasi = "Turki"

if tabungan_juta >= 200 and (berat_badan >= 65 and berat_badan <= 68) :
    print("MISI BERHASIL !! Siap berangkat ke Korea !")

    elif tabungan_juta >= 100 or lokasi == "Indonesia" :
        print("Jangan sampai ke-distraksi !")

        elif tabungan_juta < 50 and lokasi == "Turki" :
            # Contoh Nested IF (Logika dalam Logika)
            if berat_badan < 60 :
                print("PERINGATAN: Tabungan tipis & kurus. Makan yang banyak !!")
            else :
                print("Survival Mode, Brooo !! Fokus kerja dan nabung dulu.")

                else :
                    print("Jangan kasih kendor, Seo-Jin! Bentar lagi nyampai finish kok.")
```