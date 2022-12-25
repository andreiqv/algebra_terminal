from mult_table import lm_beta

dim = 3
N = dim

map3indto1 = {}
count = 1
# numeration from 1
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(j, N+1):
            map3indto1[(i,j,k)] = count
            count += 1

print(map3indto1)
DIM_WN = len(map3indto1)
print("DIM(W_N) =", DIM_WN)


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

print(map3to1)
print(map1to3)
for i in map1to3:
    print(i, map1to3[i])
#sys.exit()


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