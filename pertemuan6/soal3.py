nilaiUjian = int(input("Masukkan nilai ujian: "))
penghasilan = int(input("Masukkan penghasilan orang tua: Rp."))

if (nilaiUjian > 90) and (penghasilan < 2000000):
    print('Anda mendapat beasiswa penuh')
elif (90 >= nilaiUjian > 80) and (penghasilan < 4000000):
    print('Anda mendapat beasiswa parsial')
else:
    print('Anda tidak mendapat beasiswa')