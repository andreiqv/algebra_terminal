import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(threshold=np.inf)

from numpy import matrix


def get_matrix(a,b,c,d,e,f):

    X = matrix([
        [ 0 , - 2*a , 0 , 0 , 0 , 0 ],
        [ 0 , b , - a , 0 , 0 , 0 ],
        [ 0 , 0 , 2*b , 0 , 0 , 0 ],
        [ a , 0 , 0 , - b , - 2*a , 0 ],
        [ 0 , a , 0 , 0 , 0 , - a ],
        [ 0 , 0 , a , 0 , 0 , b ],
    ])

    # From the paper:
    """
    X = matrix([
        [ 0 , a , 0   , 0 , 0 , 0 ],
        [ 0 , b , 2*a , 0 , 0 , 0 ],
        [ 0 , 0 , 2*b , 0 , 0 , 0 ],
        [-a , 0 , 0   ,-b , a , 0 ],
        [ 0 ,-a , 0   , 0 , 0 , 2*a ],
        [ 0 , 0 ,-a   , 0 , 0 , b ],
    ])
    """
    return X


def print_matrix(A):

    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            print(" {:2d}".format(A[i,j]), end="")
        print()

def com(A,B): 
    """ commutator
    """
    return A*B - B*A


if __name__ == "__main__":

    A = get_matrix(1,0,0,0,0,0)
    B = get_matrix(0,1,0,0,0,0)
    Z = get_matrix(0,0,0,0,0,0)
    print("A:")
    print(A)
    print("B:")
    print(B)
    print("-----")
    #print_matrix(com(A,C))
    V = com(A,B)
    print(V)

    print("A*B=A",(com(A,B) == A).all())
    ls = ["Z", "A", "B", "C", "D", "E", "F"]
    n = lambda i: ls[i]

    if (V == Z).all():
        print("V = 0")
    else:
        for i, M1 in enumerate([Z,A,B]):
            for j, M2 in enumerate([Z,A,B]):
                if (V == M1 + M2).all():
                    print(f"V = {n(i)} + {n(j)}")
                if (V == M1 - M2).all():
                    print(f"V = {n(i)} - {n(j)}")
                if (V == - M1 + M2).all():
                    print(f"V = - {n(i)} + {n(j)}")
                if (V == - M1 - M2).all():
                    print(f"V = - {n(i)} - {n(j)}")