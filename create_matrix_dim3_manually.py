import numpy as np
import re

size = 18

def replace(x):

    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            if type(x[i,j]) == str:
                if len(x[i,j]) > 0:
                    #print(i,j)
                    #print(x[i,j])
                    s = x[i,j]
                    s = s.replace(r"x[15,17]", "a")
                    s = s.replace(r"x[17,17]", "b")
                    s = s.replace(r"x[18,6]",  "c")
                    s = s.replace(r"x[18,12]", "d")
                    s = s.replace(r"x[18,17]", "e")
                    s = s.replace(r"x[18,18]", "f")
                    x[i,j] = s
                    #print(s)
    return x

def create_array():

    x = np.zeros((size+1, size+1), dtype=object)

    x[15,17] = "a"
    x[17,17] = "b"
    x[18,6] = "c"
    x[18,12] = "d"
    x[18,17] = "e"
    x[18,18] = "f"


    x[1,2] = "2a"
    x[1,3] = "- 2c"
    x[2,2] = "b"
    x[2,3] = "- d"
    x[2,4] = "a"
    x[2,5] = "- c"
    x[3,3] = "f"
    x[3,5] = "a"
    x[3,6] = "- c"
    x[4,4] = "2b"
    x[4,5] = "- 2d"
    x[5,5] = "b + f"
    x[5,6] = "- d"
    x[6,5] = "e"
    x[6,6] = "2f"
    x[7,1] = "- a"
    x[7,7] = "- b"
    x[7,8] = "2a"
    x[7,9] = "- 2c"
    x[8,2] = "- a"
    x[8,9] = "- d"
    x[8,10] = "a"
    x[8,11] = "- c"
    x[9,3] = "- a"
    x[9,9] = "- b + f"
    x[9,11] = "a"
    x[9,12] = "- c"
    x[10,4] = "- a"
    x[10,10] = "b"
    x[10,11] = "- 2d"
    x[11,5] = "- a"
    x[11,11] = "f"
    x[11,12] = "- d"
    x[12,6] = "- a"
    x[12,11] = "e"
    x[12,12] = "- b + 2f"
    x[13,1] = "c"
    x[13,7] = "d"
    x[13,13] = "- f"
    x[13,14] = "2a"
    x[13,15] = "- 2c"
    x[14,2] = "c"
    x[14,8] = "d"
    x[14,14] = "b - f"
    x[14,15] = "- d"
    x[14,16] = "a"
    x[14,17] = "- c"
    x[15,3] = "c"
    x[15,9] = "d"
    x[15,18] = "- c"
    x[16,4] = "c"
    x[16,10] = "d"
    x[16,16] = "2b - f"
    x[16,17] = "- 2d"
    x[17,5] = "c"
    x[17,11] = "d"
    x[17,18] = "- d"


    """
    x[26,24] = "a"
    x[26,26] = "b"
    x[27,27] = "c"

    x[2,2] = "b"
    x[2,4] = "a"
    x[3,3] = "- a + c"
    x[3,7] = "a"
    x[4,2] = "a"
    x[4,4] = "b"
    x[5,5] = "2a + 2b"
    x[6,6] = "b + c"
    x[6,8] = "a"
    x[7,3] = "a"
    x[7,7] = "- a + c"
    x[8,6] = "a"
    x[8,8] = "b + c"
    x[9,9] = "2c"
    x[10,10] = "- a - b"
    x[11,11] = "- a"
    x[11,13] = "a"
    x[12,12] = "- 2a - b + c"
    x[12,16] = "a"
    x[13,11] = "a"
    x[13,13] = "- a"
    x[14,14] = "a + b"
    x[15,15] = "- a + c"
    x[15,17] = "a"
    x[16,12] = "a"
    x[16,16] = "- 2a - b + c"
    x[17,15] = "a"
    x[17,17] = "- a + c"
    x[18,18] = "- a - b + 2c"
    x[19,19] = "- c"
    x[20,20] = "b - c"
    x[20,22] = "a"
    x[21,21] = "- a"
    x[21,25] = "a"
    x[22,20] = "a"
    x[22,22] = "b - c"
    x[23,23] = "2a + 2b - c"
    x[24,24] = "b"
    x[24,26] = "a"
    x[25,21] = "a"
    x[25,25] = "- a"
    """

    return x

def save_as_tex(x, path):

    full_range = range(1, x.shape[0])
    indexrange = full_range
    #indexrange = [1, 2, 4, 7, 8, 10] # subspace 1-2
    #indexrange = [1, 3, 6, 13, 15, 18] # subspace 1-3
    #indexrange = [10, 11, 12, 16, 17, 18] # subspace 2-3

    with open(path, "wt") as outfp:

        for t1, i in enumerate(indexrange):

            row = ""
            for t2, j in enumerate(indexrange):
                #print(i, j, x[i,j])
                row += " {} ".format(x[i,j])
                if t2 < len(indexrange) - 1:
                    row += "&"
                else:
                    row += "\\\\"

            print(row)
            outfp.write("{}\n".format(row))


def save_as_numpy(x, filepath):

    with open(filepath, "wt") as outfp:

        for i in range(1, x.shape[0]):

            row = "["
            for j in range(1, x.shape[1]):
                #print(i, j, x[i,j])
                row += " {} ".format(x[i,j])
                if j < x.shape[1] - 1:
                    row += ","
                else:
                    row += "],"

            print(row)
            outfp.write("{}\n".format(row))


if __name__ == "__main__":

    # from create_matrix import create_array
    x = create_array()
    x = replace(x)
    import sys
    #sys.exit()
    print(x)
    save_as_tex(x, "_matrix_out_as_tex_d3.txt")
    save_as_numpy(x, "_matrix_out_as_numpy_d3.txt")

    """
    subindices = [0,1,2,4,5,10,11,13,14] # (1,2)
    a = x[subindices,:][:,subindices]
    save_as_tex(a, "_matrix_out_as_tex_ver2_1-2.txt")

    subindices = [0,1,3,7,9,19,21,25,27]  # (1,3)
    a = x[subindices,:][:,subindices]
    save_as_tex(a, "_matrix_out_as_tex_ver2_1-3.txt")

    subindices = [0,14,15,17,18,23,24,26,27]  # (2,3)
    a = x[subindices,:][:,subindices]
    save_as_tex(a, "_matrix_out_as_tex_ver2_2-3.txt")
    """