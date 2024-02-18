# Input
tahun_lahir = int(input("Masukkan tahun lahir: "))

# Proses
from datetime import date

today = date.today()
tahun_sekarang = today.year

if tahun_sekarang < tahun_lahir:
  raise ValueError("Tahun lahir tidak boleh lebih besar dari tahun sekarang.")

umur = tahun_sekarang - tahun_lahir

# Output
print(f"Umur: ", umur)
