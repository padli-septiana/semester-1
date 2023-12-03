# Nama : Muhammad Padli Septiana
# Kelas : RPL 1Z

barang = [
    {
        'nama': 'Sepatu Pantofel',
        'size': 39,
        'stok': 3,
    },
    {
        'nama': 'Sepatu Pantofel',
        'size': 40,
        'stok': 10,
    },
    {
        'nama': 'Sepatu Pantofel',
        'size': 41,
        'stok': 9,
    },
    {
        'nama': 'Sepatu Pantofel',
        'size': 42,
        'stok': 11,
    },
    {
        'nama': 'Sepatu Pantofel',
        'size': 43,
        'stok': 15,
    },
    {
        'nama': 'Sepatu Converse',
        'size': 39,
        'stok': 3,
    },
    {
        'nama': 'Sepatu Converse',
        'size': 40,
        'stok': 10,
    },
    {
        'nama': 'Sepatu Converse',
        'size': 41,
        'stok': 9,
    },
    {
        'nama': 'Sepatu Converse',
        'size': 42,
        'stok': 11,
    },
    {
        'nama': 'Sepatu Converse',
        'size': 43,
        'stok': 15,
    },
    {
        'nama': 'Sepatu Aerostreet',
        'size': 39,
        'stok': 3,
    },
    {
        'nama': 'Sepatu Aerostreet',
        'size': 40,
        'stok': 10,
    },
    {
        'nama': 'Sepatu Aerostreet',
        'size': 41,
        'stok': 9,
    },
    {
        'nama': 'Sepatu Aerostreet',
        'size': 42,
        'stok': 11,
    },
    {
        'nama': 'Sepatu Aerostreet',
        'size': 43,
        'stok': 15,
    },
]

# Make function for searching
def search(key, things):
    while True:
        result = []

        for i in things:
            if key.lower() in i['nama'].lower():
                result.append(i)

        if len(result) > 0:
            for i in result:
                print(f"{i['nama']}")
                print(f"Nomor {i['size']}")
                print(f"Stok {i['stok']}")
            break
        else:
            print('Tidak ditemukan')
            break

key = input('Cari nama barang: ')
search(key, barang)