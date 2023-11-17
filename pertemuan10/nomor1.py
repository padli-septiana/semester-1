# Muhammad Padli Septiana
# 2302061
# RPL 1A

import numpy as np

suhuC = np.array([29, 28, 29, 27, 28, 27, 28, 29, 27, 29])
suhuF = suhuC.copy()
i=0

for f in suhuC:
    suhuF[i] = (9/5 * f) + 32
    i += 1

i=0
for s in suhuF:
    print(f'Suhu hari ke-{i+1} : {suhuF[i]} Fareinheit')
    i += 1