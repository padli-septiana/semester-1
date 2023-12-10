# Nama : Muhammad Padli Septiana
# NIM : 2302061
# Kelas : RPL - 1A

import random

while True:
    print("1. Ambil antrian")
    print("2. Input antrian")
    print("0. Keluar")

    menu = int(input("Pilih menu: "))
    if menu == 1:
        antrian = random.randint(1, 10)
        print("Antrian anda: ", antrian)
    if menu == 2:
        print("Antrian sekarang: ", antrian)
        inputAntrian = int(input("Masukkan antrian anda: "))
        if inputAntrian == antrian:
            print("Silahkan masuk")
            break
        else:
            print("Mohon menunggu, antrian anda belum tiba")

    if menu == 0:
        break