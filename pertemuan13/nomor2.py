# Nama : Muhammad Padli Septiana
# NIM : 2302061
# Kelas : RPL - 1A

import numpy as np

jumlahElemen = int(input("Masukkan jumlah elemen array: "))
numbers = np.array([int(input("Masukkan angka: ")) for i in range(jumlahElemen)])

cariNilai = int(input("Masukkan angka yang ingin dicari: "))
if cariNilai in numbers:
    print(cariNilai)
else:
    print("Maaf nilai yang dicari tidak ada di array")