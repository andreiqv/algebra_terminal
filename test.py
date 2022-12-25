"""
lower indices for alpha

alpha_{ijk} * alpha_{lmn} = sum_{pqr} lambda^{pqr}_{ijklmn} alpha_{pqr}
"""

import sys


N = 2
map3to1 = {}
map1to3 = {}

index = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(j, N+1):
            map3to1[(i,j,k)] = index
            map1to3[index] = (i,j,k)
            index += 1

print(map3to1)
print(map1to3)
for i in map1to3:
    print(i, map1to3[i])


#sys.exit()
print()
print()


irange = [1,2]

count = 0

for i in irange:
    for j in irange:
        for k in irange:

            for l in irange:
                for m in irange:
                    for n in irange:

                        for p in irange:
                            for q in irange:
                                for r in irange:

                                    if j > k or m > n or q > r:
                                        continue

                                    I = map3to1[(i,j,k)]
                                    L = map3to1[(l,m,n)]
                                    P = map3to1[(p,q,r)]
                                    #print(I,L,P)

                                    #print("p,q,r:", p,q,r)
                                    print("count:", count, I,L,P)
                                    count += 1

