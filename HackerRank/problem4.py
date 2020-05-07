mport math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    output=""
    s=s.replace(" ", "")
    n=len(s)
    r=math.floor(math.sqrt(n))
    if(r>=math.sqrt(n)):
        c=r
    else:
        c=r+1
    for j in range(c):
        for i in range(j,n,c):
            output+=s[i]
        output+=" "
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
