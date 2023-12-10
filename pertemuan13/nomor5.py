# Nama : Muhammad Padli Septiana
# NIM : 2302061
# Kelas : RPL - 1A

menuResto = [
    ["Ayam gulai", "Tersedia"],
    [ "Babat", "Tersedia"], 
    ["Cumi", "Tersedia"],
    ["Ikan kembung", "Tidak Tersedia"],
    ["Kikil", "Tersedia"],
    ["Limpa", "Tidak Tersedia"],
    ["Otak", "Tidak Tersedia"],
    ["Paru", "Tersedia"],
    ["Rendang", "Tidak Tersedia"],
    ["Telur", "Tersedia"],
    ["Usus" "Tersedia"]
]

for i in range(len(menuResto)):
    print(f"{i+1}. {menuResto[i]}")

pilihMenu = int(input("Masukkan nomor menu yang ingin dipesan: "))

print(f"{menuResto[pilihMenu-1][0]} {menuResto[pilihMenu-1][1]}")