# Muhammad Padli Septiana
# 2302061
# RPL - 1A

def totalNilai(nilai):
    return sum(nilai)

def ratarataNilai(nilai):
    return sum(nilai) / len(nilai)
    
nilai = input("Masukkan nilai dan pisahkan nilai dengan spasi: ").split()
nilai = [int(x) for x in nilai]

print("Total nilai adalah:", totalNilai(nilai))
print("Rata-rata nilai adalah:", ratarataNilai(nilai))