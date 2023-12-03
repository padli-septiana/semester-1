# Nama : Muhammad Padli Septiana
# Kelas : RPL 1Z

import time

def linearSearch(key, things):
    while True:
        result = []

        for i in things:
            if key == i:
                result.append(i)

        if len(result) > 0:
            return result
        else:
            print('Tidak ditemukan')
            break

def binarySearch(key, things):
    while True:
        result = []

        for i in things:
            if key == i:
                result.append(i)

        if len(result) > 0:
            return result
        else:
            print('Tidak ditemukan')
            break

array = [1, 2, 5, 7, 8, 10, 16, 18, 19, 23, 24, 26, 28, 29, 32, 33, 34, 35, 36, 38, 40, 41, 42, 43, 44, 46, 48, 49, 51, 55, 57, 58, 59, 60, 63, 65, 66, 69, 74, 75, 76, 77, 78, 79, 81, 82, 85, 90, 93, 100]

start_time = time.time()
print(binarySearch(60, array))
end_time = time.time()

# print(start_time, end_time)
execution_time = end_time - start_time
print(f"Execution time linear search: {execution_time} seconds")

