# Nama : Muhammad Padli Septiana
# Kelas : RPL 1Z

mahasiswa = [
    {"nama": "John Doe", "nim": "1234567"},
    {"nama": "Jane Smith", "nim": "2345678"},
    {"nama": "Michael Johnson", "nim": "3456789"},
    {"nama": "Emily Davis", "nim": "4567890"},
    {"nama": "Daniel Wilson", "nim": "5678901"},
    {"nama": "Olivia Taylor", "nim": "6789012"},
    {"nama": "David Anderson", "nim": "7890123"},
    {"nama": "Sophia Martinez", "nim": "8901234"},
    {"nama": "Matthew Robinson", "nim": "9012345"},
    {"nama": "Emma Clark", "nim": "0123456"},
    {"nama": "Joseph Rodriguez", "nim": "1234567"},
    {"nama": "Ava Lewis", "nim": "2345678"},
    {"nama": "Andrew Lee", "nim": "3456789"},
    {"nama": "Isabella Walker", "nim": "4567890"},
    {"nama": "William Hall", "nim": "5678901"},
    {"nama": "Mia Young", "nim": "6789012"},
    {"nama": "James Allen", "nim": "7890123"},
    {"nama": "Sofia Hernandez", "nim": "8901234"},
    {"nama": "Benjamin King", "nim": "9012345"},
    {"nama": "Charlotte Green", "nim": "0123456"}
]
    
def search(key, things):
    while True:
        result = []

        for i in things:
            if key.lower() in i['nama'].lower():
                result.append(i)

        if len(result) > 0:
            return result
        else:
            print('Tidak ditemukan')
            break

def printArray(array):
    for i in array:
        print(f"{i['nama']} - {i['nim']}")

key = input("Masukkan nama: ")
printArray(search(key, mahasiswa))
