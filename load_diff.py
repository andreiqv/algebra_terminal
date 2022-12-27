import sys
import json
import numpy as np
import re
from transform_system import transform_system


from indexation import N, dim, ind3to1, DIM_WN
from indexation import ind2to1, ind1to2

#index_range = list(range(1, dim + 1))
#irange = range(1, dim + 1)
#zero_vector = [0] * dim

print("DIM_WN:", DIM_WN)


def load_data(path):

    with open(path) as fp:
        data = json.load(fp)
    return data


"""
def ind1to2(i):
    i1 = i // DIM_WN + 1
    i2 = i % DIM_WN + 1
    return (i1,i2)
"""

def make_eq_system(data):

    eq_system = []

    rref0 = data.get("rref0")
    rref1 = data.get("rref1")
    #print(rref1)
    #num_d_ind = (dim**3)**2
    num_d_ind = DIM_WN**2

    all_indices = set(range(num_d_ind))
    print("all_indices:", all_indices)
    print("set(rref1):", set(rref1))
    indep = list(all_indices - set(rref1))
    indep.sort()
    print("indepedent:", indep)

    for i, row in enumerate(rref0):
        i1, i2 = ind1to2(i)
        print(f"{i}({i1},{i2}): {row}")

        eq = ""
        count = 0
        for j, coef in enumerate(row):

            if coef != 0:
                count += 1
                j1, j2 = ind1to2(j)
                #eq += " + ({})*x_{},{}".format(coef, j1, j2)
                if coef == 1:
                    eq += " + x[{},{}]".format(j1, j2)
                elif coef == -1:
                    eq += " - x[{},{}]".format(j1, j2)
                elif coef < 0:
                    eq += " - {}*x[{},{}]".format(abs(coef), j1, j2)
                else:
                    eq += " + {}*x[{},{}]".format(coef, j1, j2)

                if j == 75:
                    sys.exit()
        
        if count > 1:
            if i < num_d_ind or eq != "":
                eq = eq.strip().strip("+").strip()
                print("{} = 0".format(eq))
                eq_system.append(eq)
                #print("{}(({},{})): {} = 0".format(i + 1, i1, i2, eq))

    print("indep:", indep)
    indep_str_list = ["x_({},{})".format(*ind1to2(i)) for i in indep]
    print(indep_str_list)
    for i in indep:
        print("x[{0},{1}] = \"x[{0},{1}]\"".format(*ind1to2(i)))
    print()

    return eq_system, indep_str_list


if __name__ == "__main__":

    if dim == 2:
        #path = "rref.txt"
        #path = "rref_beta_dim2.txt"
        path = "rref_beta_dim2_reverse.txt"
        #path = "rref_alpha_dim2.txt"
    elif dim == 3:
        #path = "rref.txt"
        #path = "rref_beta_dim3_reverse.txt"
        path = "rref_beta_dim3.txt"

    data = load_data(path)

    eq_system, indep_str_list = make_eq_system(data)

    print("------------------")
    for eq in eq_system:
        print(eq)
    print("indep_str_list:", indep_str_list)


    #eq_system = ["x[6,6] - x[26,26] - x[27,27]"]
    #print("in:", eq_system)
    eq_system = transform_system(eq_system, dim)

    with open("_out_system_tex.txt", "wt") as outfp:
        for eq in eq_system:
            outfp.write("${}$,\\\\\n".format(eq.replace('"','')))

    with open("_out_system.txt", "wt") as outfp:
        for eq in eq_system:
            outfp.write("{}\n".format(eq))