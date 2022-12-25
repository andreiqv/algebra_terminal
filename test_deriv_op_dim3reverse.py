import numpy as np
from numpy import matrix
from indexation import lm3
import sys

DIM_WN = 18

def mul(vec1, vec2):
    output = np.zeros(DIM_WN, dtype=np.int64)
    for I in range(1, DIM_WN+1):
        for L in range(1, DIM_WN+1):
            #print()
            #print(vec1.transpose())
            #print(vec2.transpose())
            #print(vec1.shape)
            k1 = vec1[I-1,0]
            k2 = vec2[L-1,0]
            vec = [k1*k2*lm3(P, I, L) for P in range(1, DIM_WN+1)]
            #print(f"I={I}, L={L}: k1={k1}, k2={k2}, vec={vec}")
            output += np.array(vec)
            #sys.exit()
    return np.matrix(output).transpose()


def get_D(a,b,c,d,e,f):

    X = matrix([
        [ 0 , 0 , 0 , 0 , 0 , 0 , - a , 0 , 0 , 0 , 0 , 0 , - d , 0 , 0 , 0 , 0 , 0 ],
        [ 2*a , b , - c , 0 , 0 , 0 , 0 , - a , 0 , 0 , 0 , 0 , 0 , - d , 0 , 0 , 0 , 0 ],
        [ 2*d , e , f , 0 , 0 , 0 , 0 , 0 , - a , 0 , 0 , 0 , 0 , 0 , - d , 0 , 0 , 0 ],
        [ 0 , a , 0 , 2*b , - c , 0 , 0 , 0 , 0 , - a , 0 , 0 , 0 , 0 , 0 , - d , 0 , 0 ],
        [ 0 , d , a , 2*e , b + f , - 2*c , 0 , 0 , 0 , 0 , - a , 0 , 0 , 0 , 0 , 0 , - d , 0 ],
        [ 0 , 0 , d , 0 , e , 2*f , 0 , 0 , 0 , 0 , 0 , - a , 0 , 0 , 0 , 0 , 0 , - d ],
        [ 0 , 0 , 0 , 0 , 0 , 0 , - b , 0 , 0 , 0 , 0 , 0 , - e , 0 , 0 , 0 , 0 , 0 ],
        [ 0 , 0 , 0 , 0 , 0 , 0 , 2*a , 0 , - c , 0 , 0 , 0 , 0 , - e , 0 , 0 , 0 , 0 ],
        [ 0 , 0 , 0 , 0 , 0 , 0 , 2*d , e , - b + f , 0 , 0 , 0 , 0 , 0 , - e , 0 , 0 , 0 ],
        [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , a , 0 , b , - c , 0 , 0 , 0 , 0 , - e , 0 , 0 ],
        [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , d , a , 2*e , f , - 2*c , 0 , 0 , 0 , 0 , - e , 0 ],
        [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , d , 0 , e , - b + 2*f , 0 , 0 , 0 , 0 , 0 , - e ],
        [ 0 , 0 , 0 , 0 , 0 , 0 , c , 0 , 0 , 0 , 0 , 0 , - f , 0 , 0 , 0 , 0 , 0 ],
        [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , c , 0 , 0 , 0 , 0 , 2*a , b - f , - c , 0 , 0 , 0 ],
        [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , c , 0 , 0 , 0 , 2*d , e , 0 , 0 , 0 , 0 ],
        [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , c , 0 , 0 , 0 , a , 0 , 2*b - f , - c , 0 ],
        [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , c , 0 , 0 , d , a , 2*e , b , - 2*c ],
        [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , c , 0 , 0 , d , 0 , e , f ],
    ])
    """ from article:
    X = matrix([
        [ 0 , a ,  0 ,  0 , 0 , 0 ],
        [ 0 , b , 2*a , 0 , 0 , 0 ],
        [ 0 , 0 , 2*b , 0 , 0 , 0 ],
        [ -a , 0 , 0 , -b , a , 0 ],
        [ 0 , -a , 0 , 0 , 0 , 2*a ],
        [ 0 , 0 , -a , 0 , 0 ,  b ],
    ])
    """
    print("X:")
    print(X)

    #return X.transpose()
    return X


def get_basis(dim):
    basis = []
    for i in range(dim):
        vec = np.zeros(dim, dtype=np.int64)
        vec[i] = 1
        m = matrix(vec)
        basis.append(m.transpose())
    return basis


if __name__ == "__main__":

    P = 4
    I = 2
    L = 2
    print(lm3(P, I, L))

    #sys.exit()

    print("-------------")
    D = get_D(1, 2, 3, 4, 5, 6)
    print(D)
    basis = get_basis(dim=DIM_WN)
    #print(basis)
    #print()

    e1 = basis[0]
    e2 = basis[1]
    e3 = basis[2]
    e4 = basis[3]
    e5 = basis[4]
    e6 = basis[5]
    e7 = basis[6]
    e8 = basis[7]
    e9 = basis[8]
    e10 = basis[9]
    e11 = basis[10]
    e12 = basis[11]
    e13 = basis[12]
    e14 = basis[13]
    e15 = basis[14]
    e16 = basis[15]
    e17 = basis[16]
    e18 = basis[17]

    for i, vec in enumerate(basis):
        res = D * vec
        print(i+1)
        print(vec.transpose())
        print(res.transpose())

    #print()
    #for i in range(DIM_WN):
    #    for j in range(DIM_WN):
    #        out = mul(basis[i], basis[j])
    #        print(i+1, j+1, out.transpose())
    #print()
    #sys.exit()

    print()
    print("e1*e1=", mul(e1, e1).transpose())
    print("e1*e2=", mul(e1, e2).transpose())
    print("e2*e2=", mul(e2, e2).transpose())
    print("e3*e3=", mul(e3, e3).transpose())

    #sys.exit()
    v = e3
    u = e9

    print()
    print(D)
    print("v=", v.transpose())
    print("u=", u.transpose())
    print("D(v)=", (D * v).transpose())
    print("D(u)=", (D * u).transpose())
    print("v*u=", (mul(v, u)).transpose())
    print("D(v*u)=", (D * mul(v, u)).transpose())
    print("D(v)*u=", (mul(D * v, u)).transpose())
    print("v*D(u)=", (mul(v, D * u)).transpose())

    print()
    t1 = D * mul(v, u)
    t2 = mul(D * v, u) + mul(v, D * u)
    print("t1:", t1.transpose())
    print("t1:", t2.transpose())
    #sys.exit()

    i = 1
    j = 1
    t1 = D * mul(basis[i], basis[j])
    t2 = mul(D * basis[i], basis[j]) + mul(basis[i], D * basis[j])
    print(t1.transpose())
    print(t2.transpose())
    #print((t1 -t2).transpose())
    print(np.array_equal(t1, t2))


    #sys.exit()
    print("------------------")
    for i in range(DIM_WN):
        for j in range(DIM_WN):
            t1 = D * mul(basis[i], basis[j])
            t2 = mul(D * basis[i], basis[j]) + mul(basis[i], D * basis[j])
            #print(t1.transpose())
            #print(t2.transpose())
            #print((t1 -t2).transpose())
            print(i+1,j+1, np.array_equal(t1, t2))
