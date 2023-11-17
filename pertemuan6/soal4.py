nama = input('Masukkan nama: ')
gaji = int(input('Masukkan gaji: Rp.'))
print(f'Bagaimana performa {nama} dalam bekerja?')
print('1. Sangat Baik')
print('2. Baik')
print('3. Cukup')

performa = int(input('Masukkan antara 1-3: '))

if performa == 1:
    print(f'{nama} mendapatkan bonus sebesar Rp.{int(gaji*0.2)}')
elif performa == 2:
    print(f'{nama} mendapatkan bonus sebesar Rp.{int(gaji*0.1)}')
elif performa == 3:
    print(f'{nama} mendapatkan bonus sebesar Rp.{int(gaji*0.05)}')
else:
    print('Maaf input yang anda masukkan salah')