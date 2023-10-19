totalBelanja = int(input("Total belanja: Rp."))

print(f"Total belanja anda adalah Rp.{totalBelanja}")

if totalBelanja > 500000:
    print(f"Selamat anda mendapatkan diskon sebesar 10%")
    print(f"Total yang harus anda bayar adalah Rp.{int(totalBelanja*0.9)}")
else:
    print("Maaf anda tidak mendapatkan diskon")