def delta(i,j):
    return 1 if i == j else 0


def lm_alpha(p,q,r, i,j,k, l,m,n):
    d = delta
    lm = d(j,1) * ( d(k,l)*d(p,i)*d(q,m)*d(r,n) - d(m,i)*d(p,l)*d(q,k)*d(r,n) - d(n,i)*d(p,l)*d(q,m)*d(r,k) )
    return lm


def lm_beta(p,q,r, i,j,k, l,m,n):
    d = delta
    f1 = d(j,1) * ( d(k,l)*d(p,i)*d(q,m)*d(r,n) - d(m,i)*d(p,l)*d(q,k)*d(r,n) - d(n,i)*d(p,l)*d(q,m)*d(r,k) )
    f2 = d(k,1) * ( d(j,l)*d(p,i)*d(q,m)*d(r,n) - d(m,i)*d(p,l)*d(q,j)*d(r,n) - d(n,i)*d(p,l)*d(q,m)*d(r,j) )
    #print(f"f1={f1}")
    #print(f"f2={f2}")
    lm = (f1 + f2) // 2
    return lm


def lm_gamma(p,q,r, i,j,k, l,m,n):
    d = delta
    lm = d(j,1) * ( d(k,l)*d(p,i)*d(q,m)*d(r,n) - d(m,i)*d(p,l)*d(q,k)*d(r,n) - d(n,i)*d(p,l)*d(q,m)*d(r,k) )\
        - d(k,1) * ( d(j,l)*d(p,i)*d(q,m)*d(r,n) - d(m,i)*d(p,l)*d(q,j)*d(r,n) - d(n,i)*d(p,l)*d(q,m)*d(r,j) )
    return lm


def lm_v02(p,q,r, i,j,k, l,m,n):
    d = delta
    if j == 1:
        return d(k,l)*d(p,i)*d(q,m)*d(r,n) - d(m,i)*d(p,l)*d(q,k)*d(r,n) - d(n,i)*d(p,l)*d(q,m)*d(r,k)
    else:
        return 0


def lm_v01(p,q,r, i,j,k, l,m,n):
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


lm = lm_v02


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