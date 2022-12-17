import sys


def delta(i,j):
    return 1 if i == j else 0


def lm_alpha(p,q,r, i,j,k, l,m,n):
    d = delta
    lm = d(j,1) * ( d(k,l)*d(p,i)*d(q,m)*d(r,n) - d(m,i)*d(p,l)*d(q,k)*d(r,n) - d(n,i)*d(p,l)*d(q,m)*d(r,k) )
    return lm


def lm_beta_0(p,q,r, i,j,k, l,m,n):
    d = delta
    f1 = d(j,1) * ( d(k,l)*d(p,i)*d(q,m)*d(r,n) - d(m,i)*d(p,l)*d(q,k)*d(r,n) - d(n,i)*d(p,l)*d(q,m)*d(r,k) )
    f2 = d(k,1) * ( d(j,l)*d(p,i)*d(q,m)*d(r,n) - d(m,i)*d(p,l)*d(q,j)*d(r,n) - d(n,i)*d(p,l)*d(q,m)*d(r,j) )
    #print(f"f1={f1}")
    #print(f"f2={f2}")
    lm = f1 + f2
    return lm


def lm_beta_sym(p,q,r, i,j,k, l,m,n):
    
    if q == r:
        return lm_beta_0(p,q,r, i,j,k, l,m,n)
    else:
        return lm_beta_0(p,q,r, i,j,k, l,m,n) + lm_beta_0(p,r,q, i,j,k, l,m,n)
    

    return lm



def lm_beta_v2(p,q,r, i,j,k, l,m,n):
    d = delta
    f1 = d(j,1) * ( d(k,l)*d(p,i)*d(q,m)*d(r,n) - d(m,i)*d(p,l)*d(q,k)*d(r,n) - d(n,i)*d(p,l)*d(q,m)*d(r,k) )
    f2 = d(k,1) * ( d(j,l)*d(p,i)*d(q,m)*d(r,n) - d(m,i)*d(p,l)*d(q,j)*d(r,n) - d(n,i)*d(p,l)*d(q,m)*d(r,j) )
    #print(f"f1={f1}")
    #print(f"f2={f2}")
    lm = (f1 + f2)

    if q == r:
        lm = lm * 2

    if j == k:
        lm = lm / 2
    if m == n:
        lm = lm / 2

    #if lm != f1 + f2:
    #    print(p,q,r, i,j,k, l,m,n)
    #    print("f1+f2:", f1+f2)
    #    print("lm:", lm)
    #    sys.exit()

    return lm

lm_beta = lm_beta_sym



def lm_gamma(p,q,r, i,j,k, l,m,n):
    d = delta
    lm = d(j,1) * ( d(k,l)*d(p,i)*d(q,m)*d(r,n) - d(m,i)*d(p,l)*d(q,k)*d(r,n) - d(n,i)*d(p,l)*d(q,m)*d(r,k) )\
        - d(k,1) * ( d(j,l)*d(p,i)*d(q,m)*d(r,n) - d(m,i)*d(p,l)*d(q,j)*d(r,n) - d(n,i)*d(p,l)*d(q,m)*d(r,j) )
    return lm


def lm_alpha_v02(p,q,r, i,j,k, l,m,n):
    d = delta
    if j == 1:
        return d(k,l)*d(p,i)*d(q,m)*d(r,n) - d(m,i)*d(p,l)*d(q,k)*d(r,n) - d(n,i)*d(p,l)*d(q,m)*d(r,k)
    else:
        return 0


def lm_alpha_v03(p,q,r, i,j,k, l,m,n):
    if j != 1:
        return 0

    t = 0

    if p == q == r == m == n == l == k == i:
        t += 1
        return -1

    if p == l and q == r == m == n == k == i and l != i:
        t += 1
        return -2

    if p == i and q == m and r == n and k == l and l != i:
        t += 1
        return 1

    if p == i and q == m and r == n and k == l and m != k and n != k:
        t += 1
        return 1

    if p == l and q == k and r == n and m == i and m != k:
        t += 1
        return -1

    if p == l and q == k and r == n and m == i and l != i and n != k:
        t += 1
        return -1

    if p == l and q == m and r == k and n == i and n != k:
        t += 1
        return -1

    if p == l and q == m and r == k and n == i and l != i and m != k:
        t += 1
        return -1

    
    assert t <= 1

    return 0


lm = lm_alpha


"""
DIM_WN = 6
def mult_vectors(vec1, vec2):
    output = np.zeros(DIM_WN)
    for I in range(1, DIM_WN+1):
        for L in range(1, DIM_WN+1):
            k1 = vec[I]
            k2 = vec[L]
            vec = [lm3(P, I, L) for P in range(1, DIM_WN+1)]
            output += np.array(vec)
    return output
"""


if __name__ == "__main__":

    lm_a = lm_alpha(1,1,1, 1,1,1, 1,1,1)
    lm_b = lm_beta(1,1,1, 1,1,1, 1,1,1)
    lm_g = lm_gamma(1,1,1, 1,1,1, 1,1,1)

    print("lm_a:", lm_a)
    print("lm_b:", lm_b)
    print("lm_g:", lm_g)

    lm_b = lm_beta(1,1,2, 2,1,1, 1,2,2)
    print("lm_b:", lm_b)

    print("Test mult table:")
    for p in [1,2]:
        for q in [1,2]:
            for r in [1,2]:
                l = lm(p=p,q=q,r=r, i=2,j=1,k=1, l=2,m=1,n=2)
                print("{}{}{}: l={}".format(p,q,r,l))

    print()
    print(lm_beta(2,1,1, 2,1,2, 2,1,1))

    print()

    """
    DIM_WN = 6
    for I in range(1,DIM_WN+1):
        for L in range(1,DIM_WN+1):
            vec = [lm3(P, I, L) for P in range(1,DIM_WN+1)]
            print(f"e{I} * e{L} = {vec}")
    """