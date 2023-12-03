import time

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

print("\nMenggunakan Insertion Sort")
arrInsertion = [7, 1, 36, 26, 63, 93, 55, 16, 19, 38, 74, 65, 18, 59, 8, 43, 24, 79, 49, 35, 23, 78, 51, 2, 46, 28, 60, 76, 10, 85, 66, 29, 82, 58, 69, 75, 48, 100, 5, 32, 40, 33, 34, 90, 81, 42, 57, 44, 41, 77]

startTimeInsertion = time.time()
insertionSort(arrInsertion)
endTimeInsertion = time.time()

executionTimeInsertion = endTimeInsertion - startTimeInsertion
print("Execution time:", executionTimeInsertion, "seconds")