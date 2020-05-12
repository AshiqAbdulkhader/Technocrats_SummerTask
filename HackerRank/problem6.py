import math
import os
import random
import re
import sys


def nonDivisibleSubset(k, s):
    a=[]
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if(s[i]+s[j])%k!=0:
                a.append(s[i])
                a.append(s[j])
    return(len(set(a)))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
