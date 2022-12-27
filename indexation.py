from mult_table import lm_beta

dim = 3
N = dim


"""
map3indto1 = {}
count = 1
# numeration from 1
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(j, N+1):
            map3indto1[(i,j,k)] = count
            count += 1

print(map3indto1)
"""


def ind3to1(i,j,k):
    """ for beta+
    """
    return map3indto1[(i,j,k)]


def ind3to1_alpha(i,j,k):
    """ for alpha
    """
    return (i-1)*(N**2) + (j-1)*N + (k-1)*1 + 1


map3to1 = {}
map1to3 = {}

index = 1
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(j, N+1):
            map3to1[(i,j,k)] = index
            map1to3[index] = (i,j,k)
            index += 1

# new:
#print(map3to1)
#print(map1to3)
for i in map1to3:
    print(i, map1to3[i])
#sys.exit()

DIM_WN = len(map3to1)
print("DIM(W_N) =", DIM_WN)


def ind3to1(i,j,k):
    #return (i-1)*(N**2) + (j-1)*N + (k-1)*1 + 1
    return map3to1[(i,j,k)] # +1

def ind3to1from0(i,j,k):
    #return (i-1)*(N**2) + (j-1)*N + (k-1)*1 + 1
    return map3to1[(i,j,k)]

def lm3(P,I,L):
    (p,q,r) = map1to3[P]
    (i,j,k) = map1to3[I]
    (l,m,n) = map1to3[L]
    return lm_beta(p,q,r, i,j,k, l,m,n)

#---------------------------

# FOR DERIVATION MATRIX

def ind2to1(I, J):
    return DIM_WN * (I - 1) + (J - 1)


def ind1to2(i):
    i1 = i // DIM_WN + 1
    i2 = i % DIM_WN + 1
    return (i1,i2)

#-------------------------

if __name__ == "__main__":

    for i in range(1, 19):
        for j in range(1, 19):
            K = ind2to1(i, j)
            (i1,j1) = ind1to2(K)
            assert (i,j == i1,j1)
            print(f"({i},{j}) -> K={K}")

    print()
    for K in range(0, 40):
        (i1,j1) = ind1to2(K)
        print(f"K={K} -> ({i1},{j1})")