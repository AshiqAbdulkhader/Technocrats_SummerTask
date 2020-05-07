mport math
import os
import random
import re
import sys

def surfaceArea(A):
    area=0
    area=area+2*len(A)*len(A[0])
    for i in range(len(A)):
        for j in range(len(A[0])):
            area=area+A[i][j]*4
            if i>0:
                area=area-min(A[i][j],A[i-1][j])*2
            if j>0:
                area=area-min(A[i][j],A[i][j-1])*2
    return(area)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')
    fptr.close()
