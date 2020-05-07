import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

if __name__ == '__main__':
    n = int(input())

    print(extraLongFactorials(n))
