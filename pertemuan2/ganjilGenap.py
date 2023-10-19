# Menerima input dari pengguna
print("Cek Ganjil Genap")
nomer = int(input("Masukkan angka: "))

# Memeriksa apakah angka genap atau ganjil
if nomer % 2 == 0:
    print(f"{nomer} adalah angka genap.")
else:
    print(f"{nomer} adalah angka ganjil.")
