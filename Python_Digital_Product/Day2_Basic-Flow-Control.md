# BASIC FLOW CONTROL (Fondasi Pengambilan Keputusan)
     Ini adalah bab dimana program mulai bisa berpikir `Ya` atau `Tidak`.
**Materi Utama** :
    
* **The `if` Statement** : Memerintah komputer melakukan sesuatu *hanya jika syarat terpenuhi*.
* **The `else` Statement** : Rencana cadangan kalau syarat `if` tidak terpenuhi (opsional).
* **Indentasi (Spasi/The Whitespace)** : Jelaskan bahwa di Python, spasi di awal baris (Tab) itu **wajib**. Salah spasi = *Error*. Ini bedanya Python dengan bahasa lain.

**1. Apa itu **Flow Control**?**

Bayangkan kamu sedang berdiri di persimpangan jalan. Jika lampu hijau, kamu jalan. Jika merah, kamu berhenti. Inilah yang disebut *Flow Control*. Kita memberi kemampuan pada program untuk memilih jalur mana yang harus diambil berdasarkan kondisi tertentu.


**2. Anatomi **`if`** Statement :**

Syarat paling dasar adalah `if`. Ada tiga struktur bagian penting :
   
   1. **Kata Kunci `if`** : Memberitahu Python kita akan mengecek sesuatu.
   2. **Kondisi** : Sesuatu yang nilainya **Benar (True)** atau **salah (False)**. Biasanya menggunakan simbol perbandingan :
    * `>` (Lebih besar)
    * `<` (Lebih kecil)
    * `==` (Sama dengan)
   3. **Titik Dua ( : )** : Wajib ada di akhir baris `if` sebagai penanda dimulainya instruksi.
   

**3. Rahasia Terpenting : Indentasi (*Spasi*)**

Di Python, spasi di awal baris (setelah if) bukan sekedar hiasan. Spasi itu memberitahu Python : "Baris ini adalah bagian dari perintah if diatasnya." Jika tidak menjorok ke dalam, program akan error.


**4. Rencana Cadangan dengan **`else`** :**

`else` adalah jalur **alternatif**. Jika kindisi di `if` tidak terpenuhi (False), maka perintah di dalam `else` yang akan dijalankan.

**Contoh Penjelasan ke Pembeli** : 
*"Bayangkan kamu sedang mengecek saldo ATM. Jika saldo cukup, uang keluar. Jika tidak (else), muncul peringatan saldo kurang."*




## PRAKTEK KODE

```python
# Cek Saldo untuk Beli Kopi
saldo = 50000
harga_kopi = 35000

if saldo >= harga_kopi :
    print("Gass aja beli kopinya, Sikaattt!!")
    # Perhatikan baris ini menjorok ke dalam (Indentasi)
else :
    print("Kerjaa dan nabung lagi woii!!")
```