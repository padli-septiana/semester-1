import datetime
today = datetime.date.today()
year = today.year



nama_user = (input("Masukkan nama anda: "))
tahun_lahir = int(input("Masukkan tahun lahir anda: "))
umur = year - tahun_lahir
print(f"Selamat Datang {nama_user}! Umur anda sekarang adalah {umur} tahun")