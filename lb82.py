import numpy as np
import random

h = int(input("Enter h" ))
w = int(input("Enter w" ))

masa=np.zeros((h,w))
masb=np.zeros((h,w))
masx=np.zeros((1,w))

for i in range(h):
    for j in range(w):
        masa[i][j]=random.randint(1,30)

for g in range(h):
    for h in range(w):
        masb[g][h]=random.randint(31,50)
        
masc=masa+masb

for a in range(w):
    s=0
    for b in range(h):
        s+=masc[b][a]
    masx[0][a]=s 

print(masc)
print(masx)

indexs=np.where(masx[0] == min(masx[0]))[0]
for t in indexs:    
    print(masc[:, [t]])
