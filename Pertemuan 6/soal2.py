angka = input("Masukkan angka: ")

if ('1' in angka) | ('2' in angka) | ('3' in angka) | ('4' in angka) | ('5' in angka) | ('6' in angka) | ('7' in angka) | ('8' in angka) | ('9' in angka) | ('0' in angka):

    angka = int(angka)
    if angka % 2 == 0:
        print(f"Angka {angka} merupakan angka genap")
    else:
        print(f"Angka {angka} merupakan angka ganjil")

else:
    print("Maaf silahkan masukkan angka")