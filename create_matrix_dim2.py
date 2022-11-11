import numpy as np

dim = 2

def create_array():

    size = dim**3

    x = np.zeros((size+1, size+1), dtype=object)

    x[7,7] = "a" 
    x[8,8] = "b" 

    x[2,2] = "a + b"
    x[2,3] = "- a"
    x[3,2] = "- a"
    x[3,3] = "a + b"
    x[4,4] = "2b"
    x[5,5] = "- b"
    x[6,6] = "a"
    x[6,7] = "- a"
    x[7,6] = "- a"


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
    print(x)
    save_as_tex(x, "_matrix_out_as_tex_d2.txt")
    save_as_numpy(x, "_matrix_out_as_numpy_d2.txt")

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