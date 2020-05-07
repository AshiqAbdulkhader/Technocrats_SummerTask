mport math
import os
import random
import re
import sys
import collections
import itertools

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    n=len(s)
    a=[]
    count=0
    comb=list(itertools.combinations(range(n+1),2))
    for i in comb:
        a.append((str(s[i[0]:i[1]])))

    for c in itertools.combinations(a,2):
            if(sorted(c[0])==sorted(c[1])):
                count+=1
    return(count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
