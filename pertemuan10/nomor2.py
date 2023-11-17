# Muhammad Padli Septiana
# 2302061
# RPL 1A

import numpy as np
from numpy import random

nilai = random.randint(100, size=(30))
print("Nilai sebelum diurutkan:")
print(nilai, '\n')

sorted = np.sort(nilai)[::-1]
print("Nilai diurut dari terbesar:")
print(sorted, '\n')

print("5 nilai yang terbesar: ")
print(sorted[:5])