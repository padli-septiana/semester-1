# Muhammad Padli Septiana
# 2302061
# RPL - 1A

def cekPassword(pw):
    sisa = 3
    password = 'Latihan'
    
    while sisa > 0:
        if pw == password:
            print('Password benar')
            print('Login Berhasil')
            break
        else:
            print('Password salah')
            sisa -= 1
            if sisa == 0:
                print('Kesempatan habis')
                exit()
            else:
                pw = input('Masukkan password: ')


cekPassword(input('Masukkan password: '))