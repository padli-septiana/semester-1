# Nama : Muhammad Padli Septiana
# NIM : 2302061
# Kelas : RPL - 1A

import numpy as np

def Sorting(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

jumlahElemen = int(input("Masukkan jumlah elemen array: "))
numbers = np.array([int(input("Masukkan angka: ")) for i in range(jumlahElemen)])
Sorting(numbers)
print(numbers)