# Nama : Muhammad Padli Septiana
# NIM : 2302061
# Kelas : RPL - 1A


books = [
    {"kode": "A01", "judul": "Harrypotter", "penulis": "J.K. Rowling", "status": "Tersedia"},
    {"kode": "A02", "judul": "Doraemon", "penulis": "Fujiko F. Fujio", "status": "Tersedia"},
]



while True:
    print("1. Tambahkan buku")
    print("2. Pinjam buku")
    print("3. Kembalikan buku")
    print("4. Lihat buku tersedia")
    print("5. Buku yang dipinjam")
    print("0. Keluar")
    menu = int(input("Masukkan menu: "))

    if menu == 1:
        kode = input("Masukkan kode buku: ")
        judul = input("Masukkan judul buku: ")
        penulis = input("Masukkan penulis buku: ")
        status = "Tersedia"
        books.append({"kode": kode, "judul": judul, "penulis": penulis, "status": status})

    if menu == 2:
        for i in range(len(books)):
            print(f"{i+1}. {books[i]['kode']} - {books[i]['judul']} oleh {books[i]['penulis']} ({books[i]['status']})")
        pinjam = int(input("Masukkan nomor buku yang ingin dipinjam: "))
        if books[pinjam-1]["status"] == "Tersedia":
            books[pinjam-1]["status"] = "Dipinjam"
        else:
            print("Buku sedang dipinjam")

    if menu == 3:
        for i in range(len(books)):
            print(f"{i+1}. {books[i]['kode']} - {books[i]['judul']} oleh {books[i]['penulis']} ({books[i]['status']})")
        pinjam = int(input("Masukkan nomor buku yang ingin dikembalikan: "))
        books[pinjam-1]["status"] = "Tersedia"
        if books[pinjam-1]["status"] == "Dipinjam":
            books[pinjam-1]["status"] = "Tersedia"
        else:
            print("Buku tidak sedang dipinjam")

    if menu == 4:
        for i in range(len(books)):
            if books[i]["status"] == "Tersedia":
                print(f"{i+1}. {books[i]['kode']} - {books[i]['judul']} oleh {books[i]['penulis']}")

    if menu == 5:
        for i in range(len(books)):
            if books[i]["status"] == "Dipinjam":
                print(f"{i+1}. {books[i]['kode']} - {books[i]['judul']} oleh {books[i]['penulis']}")

    if menu == 0:
        break