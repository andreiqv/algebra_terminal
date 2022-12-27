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
                    s = s.replace(r"x[17,15]", "a")
                    s = s.replace(r"x[17,17]", "b")
                    s = s.replace(r"x[18,12]", "c")
                    s = s.replace(r"x[18,15]", "d")
                    s = s.replace(r"x[18,17]", "e")
                    s = s.replace(r"x[18,18]", "f")
                    x[i,j] = s
                    #print(s)
    return x

def create_array():

    x = np.zeros((size+1, size+1), dtype=object)

    x[17,15] = "x[17,15]"
    x[17,17] = "x[17,17]"
    x[18,12] = "x[18,12]"
    x[18,15] = "x[18,15]"
    x[18,17] = "x[18,17]"
    x[18,18] = "x[18,18]"

    x[1,7] = "- x[17,15]"
    x[1,13] = "- x[18,15]"
    x[2,1] = "2x[17,15]"
    x[2,2] = "x[17,17]"
    x[2,3] = "- x[18,12]"
    x[2,8] = "- x[17,15]"
    x[2,14] = "- x[18,15]"
    x[3,1] = "2x[18,15]"
    x[3,2] = "x[18,17]"
    x[3,3] = "x[18,18]"
    x[3,9] = "- x[17,15]"
    x[3,15] = "- x[18,15]"
    x[4,2] = "x[17,15]"
    x[4,4] = "2x[17,17]"
    x[4,5] = "- x[18,12]"
    x[4,10] = "- x[17,15]"
    x[4,16] = "- x[18,15]"
    x[5,2] = "x[18,15]"
    x[5,3] = "x[17,15]"
    x[5,4] = "2x[18,17]"
    x[5,5] = "x[17,17] + x[18,18]"
    x[5,6] = "- 2x[18,12]"
    x[5,11] = "- x[17,15]"
    x[5,17] = "- x[18,15]"
    x[6,3] = "x[18,15]"
    x[6,5] = "x[18,17]"
    x[6,6] = "2x[18,18]"
    x[6,12] = "- x[17,15]"
    x[6,18] = "- x[18,15]"
    x[7,7] = "- x[17,17]"
    x[7,13] = "- x[18,17]"
    x[8,7] = "2x[17,15]"
    x[8,9] = "- x[18,12]"
    x[8,14] = "- x[18,17]"
    x[9,7] = "2x[18,15]"
    x[9,8] = "x[18,17]"
    x[9,9] = "- x[17,17] + x[18,18]"
    x[9,15] = "- x[18,17]"
    x[10,8] = "x[17,15]"
    x[10,10] = "x[17,17]"
    x[10,11] = "- x[18,12]"
    x[10,16] = "- x[18,17]"
    x[11,8] = "x[18,15]"
    x[11,9] = "x[17,15]"
    x[11,10] = "2x[18,17]"
    x[11,11] = "x[18,18]"
    x[11,12] = "- 2x[18,12]"
    x[11,17] = "- x[18,17]"
    x[12,9] = "x[18,15]"
    x[12,11] = "x[18,17]"
    x[12,12] = "- x[17,17] + 2x[18,18]"
    x[12,18] = "- x[18,17]"
    x[13,7] = "x[18,12]"
    x[13,13] = "- x[18,18]"
    x[14,8] = "x[18,12]"
    x[14,13] = "2x[17,15]"
    x[14,14] = "x[17,17] - x[18,18]"
    x[14,15] = "- x[18,12]"
    x[15,9] = "x[18,12]"
    x[15,13] = "2x[18,15]"
    x[15,14] = "x[18,17]"
    x[16,10] = "x[18,12]"
    x[16,14] = "x[17,15]"
    x[16,16] = "2x[17,17] - x[18,18]"
    x[16,17] = "- x[18,12]"
    x[17,11] = "x[18,12]"
    x[17,14] = "x[18,15]"
    x[17,16] = "2x[18,17]"
    x[17,18] = "- 2x[18,12]"



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

    with open(path, "wt") as outfp:

        for i in range(1, x.shape[0]):

            row = ""
            for j in range(1, x.shape[1]):
                #print(i, j, x[i,j])
                row += " {} ".format(x[i,j])
                if j < x.shape[1] - 1:
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

    # For W_N
    #subindices = [0,1,2,4,7,8,10] # (1,2)
    #a = x[subindices,:][:,subindices]
    #save_as_tex(a, "_r_matrix_out_as_tex_ver2_1-2.txt")

    subindices = [0,1,3,6,13,15,18]  # (1,3)
    a = x[subindices,:][:,subindices]
    save_as_tex(a, "_r_matrix_out_as_tex_ver2_1-3.txt")

    #subindices = [0,14,15,17,18,23,24,26,27]  # (2,3)
    #a = x[subindices,:][:,subindices]
    #save_as_tex(a, "_r_matrix_out_as_tex_ver2_2-3.txt")

    """
    # Full W(N)
    subindices = [0,1,2,4,5,10,11,13,14] # (1,2)
    a = x[subindices,:][:,subindices]
    save_as_tex(a, "_r_matrix_out_as_tex_ver2_1-2.txt")

    subindices = [0,1,3,7,9,19,21,25,27]  # (1,3)
    a = x[subindices,:][:,subindices]
    save_as_tex(a, "_r_matrix_out_as_tex_ver2_1-3.txt")

    subindices = [0,14,15,17,18,23,24,26,27]  # (2,3)
    a = x[subindices,:][:,subindices]
    save_as_tex(a, "_r_matrix_out_as_tex_ver2_2-3.txt")
    """
