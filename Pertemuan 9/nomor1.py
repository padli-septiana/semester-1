# Muhammad Padli Septiana
# 2302061
# RPL - 1A

# Deret Fibonacci
def deretFibonacci(n):
    bilanganPertama = 0
    bilanganKedua = 1

    jumlahBilangan = 0

    while jumlahBilangan < n:
        bilanganBaru = bilanganPertama + bilanganKedua
        if jumlahBilangan == 0:
            print(bilanganPertama)
        elif jumlahBilangan == 1:
            print(bilanganKedua)
        else:
            print(bilanganBaru)
            bilanganPertama = bilanganKedua
            bilanganKedua = bilanganBaru
        jumlahBilangan += 1

banyakBilangan = int(input("Masukkan jumlah bilangan: "))
deretFibonacci(banyakBilangan)
