# Mendapatkan input dari pengguna
alas = float(input("Masukkan alas segitiga: "))
tinggi = float(input("Masukkan tinggi segitiga: "))
sisi_a = float(input("Masukkan panjang sisi A segitiga: "))
sisi_b = float(input("Masukkan panjang sisi B segitiga: "))

# Menghitung luas dan keliling segitiga
luas = (alas * tinggi) / 2
keliling = alas + sisi_a + sisi_b

# Menampilkan hasil
print("Luas segitiga adalah", luas, "satuan luas")
print("Keliling segitiga adalah", keliling, "satuan panjang")
