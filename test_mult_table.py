import sys
from indexation import N, dim, ind3to1, map3to1, map1to3, lm3
from mult_table import lm_alpha, lm_beta, lm_gamma

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


if __name__ == "__main__":

    k = lm_beta(1,1,2, 1,1,2, 1,1,1)
    print(f"k={k}")

    k = lm_beta(2,1,2, 1,1,1, 2,1,2)
    print(f"k={k}")

    #sys.exit()

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
                l = lm_alpha(p=p,q=q,r=r, i=2,j=1,k=1, l=2,m=1,n=2)
                print("{}{}{}: l={}".format(p,q,r,l))

    print()
    print(lm_beta(2,1,1, 2,1,2, 2,1,1))
    print(lm_beta(1,2,2, 1,1,2, 1,1,2))
    print(lm_beta(2,1,1, 1,1,2, 1,1,2))
    print("3-2-2:", lm3(3, 2, 2))
    print("4-2-2:", lm3(4, 2, 2))
    print()
    

    #sys.exit()
    DIM_WN = 6
    for I in range(1,DIM_WN+1):
        for L in range(1,DIM_WN+1):
            vec = [lm3(P, I, L) for P in range(1,DIM_WN+1)]
            print(f"e{I} * e{L} = {vec}")
