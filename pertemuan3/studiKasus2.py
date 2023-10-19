# Nama = Muhammad Padli Septiana
# Kelas = RPL 1A
# NIM = 2302061

# Studi Kasus 2
print("Ini studi kasus 2")
buah = ("apel", "jeruk", "ceri", "durian", "apel", "mangga")
buahList = list(buah)
buahList.pop(3)
buahList.insert(2, "manggis")
buah = tuple(buahList)
print(buah)