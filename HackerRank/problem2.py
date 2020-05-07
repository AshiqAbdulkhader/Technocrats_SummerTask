import math
import os
import random
import re
import sys
# Complete the timeInWords function below.
def timeInWords(h, m):
    t=['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
    if(m<30):
        if(m==0):
            rs=("%s o' clock"%t[h-1])
        elif(m==1):
            rs=("one minute past %s"%t[h-1])
        elif(m==15):
            rs="quarter past %s"%t[h-1]
        else:
            if(m<=20):
                rs="%s minutes past %s"%(t[m-1],t[h-1])
            else:
                a=m-(m%10)-1
                b=m%10-1
                rs="%s %s minutes past %s"%(t[a],t[b],t[h-1])

    elif(m==30):
        rs="half past %s"%t[h-1]

    else:
        if(m==45):
            rs="quarter to %s"%t[h]
        elif(m==59):
            rs="one minute to %s"%t[h]
        elif((60-m)<=20):
            rs="%s minutes to %s"%(t[60-m-1],t[h])
        else:
            a=(60-m)-(60-m)%10-1
            b=(60-m)%10-1
            rs="%s %s minutes to %s"%(t[a],t[b],t[h])

    return(rs)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
