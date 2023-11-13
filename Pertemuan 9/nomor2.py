# Muhammad Padli Septiana
# 2302061
# RPL - 1A

# Volume Tabung
def vTabung(r, t):
    hasil = (22/7) * r * r * t
    return hasil

jari = int(input("Masukkan jari-jari tabung: "))
tinggi = int(input("Masukkan tinggi tabung: "))
volume = vTabung(jari, tinggi)

print(f'Volume tabung dengan jari-jari {jari} dan tinggi {tinggi} adalah {volume}')