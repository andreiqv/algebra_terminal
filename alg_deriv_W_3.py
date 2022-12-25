import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(threshold=np.inf)

from numpy import matrix


def get_matrix(a,b,c,d,e,f):

    X = matrix([
        [ 0 , 2*a , - 2*c , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
        [ 0 , b , - d , a , - c , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
        [ 0 , 0 , f , 0 , a , - c , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
        [ 0 , 0 , 0 , 2*b , - 2*d , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
        [ 0 , 0 , 0 , 0 , b + f , - d , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
        [ 0 , 0 , 0 , 0 , e , 2*f , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
        [ - a , 0 , 0 , 0 , 0 , 0 , - b , 2*a , - 2*c , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
        [ 0 , - a , 0 , 0 , 0 , 0 , 0 , 0 , - d , a , - c , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
        [ 0 , 0 , - a , 0 , 0 , 0 , 0 , 0 , - b + f , 0 , a , - c , 0 , 0 , 0 , 0 , 0 , 0 ],
        [ 0 , 0 , 0 , - a , 0 , 0 , 0 , 0 , 0 , b , - 2*d , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
        [ 0 , 0 , 0 , 0 , - a , 0 , 0 , 0 , 0 , 0 , f , - d , 0 , 0 , 0 , 0 , 0 , 0 ],
        [ 0 , 0 , 0 , 0 , 0 , - a , 0 , 0 , 0 , 0 , e , - b + 2*f , 0 , 0 , 0 , 0 , 0 , 0 ],
        [ c , 0 , 0 , 0 , 0 , 0 , d , 0 , 0 , 0 , 0 , 0 , - f , 2*a , - 2*c , 0 , 0 , 0 ],
        [ 0 , c , 0 , 0 , 0 , 0 , 0 , d , 0 , 0 , 0 , 0 , 0 , b - f , - d , a , - c , 0 ],
        [ 0 , 0 , c , 0 , 0 , 0 , 0 , 0 , d , 0 , 0 , 0 , 0 , 0 , 0 , 0 , a , - c ],
        [ 0 , 0 , 0 , c , 0 , 0 , 0 , 0 , 0 , d , 0 , 0 , 0 , 0 , 0 , 2*b - f , - 2*d , 0 ],
        [ 0 , 0 , 0 , 0 , c , 0 , 0 , 0 , 0 , 0 , d , 0 , 0 , 0 , 0 , 0 , b , - d ],
        [ 0 , 0 , 0 , 0 , 0 , c , 0 , 0 , 0 , 0 , 0 , d , 0 , 0 , 0 , 0 , e , f ],
    ])
    return X
    #return X.transpose()


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
    C = get_matrix(0,0,1,0,0,0)
    D = get_matrix(0,0,0,1,0,0)
    E = get_matrix(0,0,0,0,1,0)
    F = get_matrix(0,0,0,0,0,1)
    Z = get_matrix(0,0,0,0,0,0)
    print("A:")
    print(A)
    print("B:")
    print(B)
    print("C:")
    print(C)
    print("D:")
    print(D)
    print("F:")
    print(F)
    print("-----")
    #print_matrix(com(A,C))
    #V = com(C,E)
    #print(V)

    M1 = C
    M2 = E
    print("M1:\n", M1)
    print("M2:\n", M2)
    print("M1*M2:\n", M1*M2)
    print("M2*M1:\n", M2*M1)

    V = com(M1,M2)
    print("M1*M2-M2*M1:", V)
    #sys.exit()

    print("A*B=A",(com(A,B) == A).all())
    print("A*C=0",(com(A,C) == Z).all())
    print("A*D=C",(com(A,D) == C).all())
    print("A*E=0",(com(A,E) == Z).all())
    print("A*F=0",(com(A,F) == Z).all())
    print("B*C=0",(com(B,C) == Z).all())
    print("B*D=D",(com(B,D) == D).all())
    print("B*E=-E",(com(B,E) == -E).all())
    print("B*F=0",(com(B,F) == Z).all())
    print("C*D=0",(com(C,D) == Z).all())
    print("C*E=?",(com(C,E) == Z).all())
    print("C*F=C",(com(C,F) == C).all())
    print("D*E=?",(com(D,E) == Z).all())
    print("D*F=D",(com(D,F) == D).all())
    print("E*F=C",(com(E,F) == -E).all())

    ls = ["Z", "A", "B", "C", "D", "E", "F"]
    n = lambda i: ls[i]

    if (V == Z).all():
        print("V = 0")
    else:
        for i, M1 in enumerate([Z,A,B,C,D,E,F]):
            for j, M2 in enumerate([Z,A,B,C,D,E,F]):
                if (V == M1 + M2).all():
                    print(f"V = {n(i)} + {n(j)}")
                if (V == M1 - M2).all():
                    print(f"V = {n(i)} - {n(j)}")
                if (V == - M1 + M2).all():
                    print(f"V = - {n(i)} + {n(j)}")
                if (V == - M1 - M2).all():
                    print(f"V = - {n(i)} - {n(j)}")