# Nama : Muhammad Padli Septiana
# NIM : 2302061
# Kelas : RPL - 1A

def sorting(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j][1] < arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

siswa = []
jumlahSiswa = int(input("Masukkan jumlah siswa: "))

for i in range(jumlahSiswa):
    nama = input("Masukkan nama siswa: ")
    nilai = int(input("Masukkan nilai siswa: "))
    siswa.append([nama, nilai])

for i in range(len(siswa)):
    print(f"{i+1}. {siswa[i][0]}")

sorting(siswa)

cariSiswa = input("Masukkan nama siswa yang ingin dicari: ")

for i in range(len(siswa)):
    if cariSiswa == siswa[i][0]:
        print(f"Nama: {siswa[i][0]}")
        if i + 1 <=3:
            print(f"Peringkat {i+1}")
        else:
            print("Siswa masih harus belajar dengan giat")
        break