"""
lower indices for alpha

alpha_{ijk} * alpha_{lmn} = sum_{pqr} lambda^{pqr}_{ijklmn} alpha_{pqr}
"""

import sys
import json
from datetime import datetime
import numpy as np
from numpy import linalg
#from mult_table import lm_alpha as lm  # for alpha
from mult_table import lm_beta as lm   # for beta+

dim = 3

N = dim
index_range = list(range(1, dim + 1))
irange = range(1, dim + 1)
zero_vector = [0] * dim

DEBUG = False

#print("zero_vector:", zero_vector)


def delta(i,j):
    return 1 if i == j else 0

def aa(k,i,j,t,m,n):
    """ aa := a(alpha^k_ij)^t_mn
    """
    return delta(k,t)*delta(i,m)*delta(j,n)


INDEXATION = 1


def get_eq_str(i,j,k, l,m,n, p,q,r):

    eq_str = ""
    flag = False
    A = [0] * ((dim**3) ** 2)

    for s in irange:
        for t in irange:
            for u in irange:

                l1 = lm(p,q,r, s,t,u, l,m,n)
                l2 = lm(p,q,r, i,j,k, s,t,u)
                l3 = lm(s,t,u, i,j,k, l,m,n)

                if INDEXATION == 3:

                    s1 = "({})*d{}{}{}{}{}{}".format(l1, s,t,u, i,j,k)
                    s2 = "({})*d{}{}{}{}{}{}".format(l2, s,t,u, l,m,n)
                    s3 = "({})*d{}{}{}{}{}{}".format(l3, p,q,r, s,t,u)
                
                else:

                    index1_d = dim**3 * (ind3to1(i,j,k) - 1) + (ind3to1(s,t,u) - 1)
                    index2_d = dim**3 * (ind3to1(l,m,n) - 1) + (ind3to1(s,t,u) - 1)
                    index3_d = dim**3 * (ind3to1(s,t,u) - 1) + (ind3to1(p,q,r) - 1)
                    
                    #print(len(A), index1_d, index2_d, index3_d)
                    A[index1_d] += l1
                    A[index2_d] += l2
                    A[index3_d] -= l3

                    if l1 != 0 or l2 != 0 or l3 != 0:
                        flag = True

                #print("{} {} {}".format(s1, s2, s3))
                #substr = "+ {} + {} - {}".format(s1, s2, s3)

    if len(eq_str) > 0 or flag:
        str_result = eq_str + " == 0 &&"
        return {'array': A, 'string': str_result}
    else:
        #return {'array': A}
        return None


def gen_eq_system():
    """
    Returns a list of coeff for one eq. and a string for one eq.
    """

    outstr = ""
    eq_list = []
    arr_list = []

    SAVE_EQ_SYS_TO_FILE = False  # for Wolfram Mathematica
    if SAVE_EQ_SYS_TO_FILE:
        fp = open("_out_equations.txt", "wt")

    for i in irange:
        for j in irange:
            for k in irange:

                for l in irange:
                    for m in irange:
                        for n in irange:

                            for p in irange:
                                for q in irange:
                                    for r in irange:

                                        result = get_eq_str(i,j,k, l,m,n, p,q,r)
                                        if result:
                                            A = result.get('array')
                                            eq_str = result.get('string')
                                            arr_list.append(A)

                                            if SAVE_EQ_SYS_TO_FILE:
                                                print(A)
                                                print(eq_str)
                                                fp.write("{}\n".format(eq_str))
                                                eq_list.append(eq_str)

    return eq_list, arr_list


def ind3to1(i,j,k):
    return (i-1)*(N**2) + (j-1)*N + (k-1)*1 + 1


# from diff_array import gen_eq_system
# eq_list, arr_list = gen_eq_system()

def generate_eq_system():
    """ Returns the matrix of lin eq system.
    """

    eq_list, arr_list = gen_eq_system()
    arr = np.array(arr_list)

    #b = np.zeros(arr.shape[0])
    #bt = b.reshape(-1,1)
    #A1 = np.concatenate((arr, bt), axis=1)
    #from sympy import Matrix
    # M1 = Matrix(A1)
    # r = M1.rref()[0]
    # rr = M1.rref()

    # np.linalg.matrix_rank(arr)
    #>>> np.linalg.matrix_rank(arr)
    #723
    #>>> np.linalg.matrix_rank(A1)
    #723

    PRINT_EQ_SYSTEM = False
    if PRINT_EQ_SYSTEM:
        d_str = "{"
        for i in irange:
            for j in irange:
                for k in irange:
                    for l in irange:
                        for m in irange:
                            for n in irange:
                                if INDEXATION == 3:
                                    d_str += "d{}{}{}{}{}{}, ".format(i,j,k, l,m,n)
                                else:
                                    d_str += "d{}u{}, ".format(ind3to1(i,j,k), ind3to1(l,m,n))
        d_str = d_str[:-2] + "}"

        print(d_str)
        print()
        print("{} variables".format(len(d_str.split(','))))
        print("{} equations".format(len(eq_list)))

    return arr


def calc():

    # a(ijk) = a^i_jk

    print(lm(p=1,q=1,r=2, i=2,j=1,k=1, l=1,m=2,n=2))

    # Need to check!!!
    print("Test mult table:")
    for p in [1,2]:
        for q in [1,2]:
            for r in [1,2]:
                l = lm(p=p,q=q,r=r, i=2,j=1,k=1, l=1,m=2,n=2)
                print("{}{}{}: l={}".format(p,q,r,l))

    #sys.exit()

    print()
    print(datetime.now())
    A = generate_eq_system()
    print("num elements:", (dim**3)**2)
    print(datetime.now())
    print("rank(A):", linalg.matrix_rank(A))
    print(datetime.now())
    #sys.exit()
    
    #num_eq = A.shape[0]
    #b = np.zeros(num_eq)
    #np.linalg.solve(A, b)

    b = np.zeros(A.shape[0], dtype=int)
    bt = b.reshape(-1,1)
    A1 = np.concatenate((A, bt), axis=1) # extension matrix

    from sympy import Matrix
    t1 = datetime.now()
    M1 = Matrix(A1)
    t2 = datetime.now()
    rref = M1.rref()
    #rr = M1.rref()
    print("rref:")
    print(rref)
    t3 = datetime.now()
    print("t1:", t1)
    print("t2:", t2)
    print("t3:", t3)

    #rref0 = rref[0].tolist()
    a = np.array(rref[0]).astype(np.int64)
    rref0 = a.tolist()
    rref1 = list(rref[1])

    #print("rref0:", rref0)
    #print("rref1:", rref1)
    #print("rref0:", type(rref0))
    #print("rref1:", type(rref1))
    outdata = {"rref0": rref0, "rref1": rref1}

    with open("rref.txt", "wt") as outfp:
        json.dump(outdata, outfp)

    return rref

if __name__ == "__main__":

    rref = calc()

