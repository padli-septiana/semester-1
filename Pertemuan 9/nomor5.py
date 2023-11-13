# Muhammad Padli Septiana
# 2302061
# RPL - 1A

def selisihWaktu(jMulai, mMulai, dMulai, jSelesai, mSelesai, dSelesai):
    if dMulai > dSelesai:
        mSelesai -= 1
        dSelesai += 60
    dSelisih = dSelesai - dMulai

    if mMulai > mSelesai:
        jSelesai -= 1
        mSelesai += 60
    mSelisih = mSelesai - mMulai

    jSelisih = jSelesai - jMulai

    selisih = [jSelisih, mSelisih, dSelisih]
    return selisih



print('Input mulai:')
jamMulai = int(input('Jam: '))
menitMulai = int(input('Menit: '))
detikMulai = int(input('Detik: '))

print('Input selesai:')
jamSelesai = int(input('Jam: '))
menitSelesai = int(input('Menit: '))
detikSelesai = int(input('Detik: '))

hasil = selisihWaktu(jamMulai, menitMulai, detikMulai, jamSelesai, menitSelesai, detikSelesai)
print(f'Selisih waktu adalah {hasil[0]} jam, {hasil[1]} menit, {hasil[2]} detik')