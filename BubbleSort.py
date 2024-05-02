#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    count = 0
    for i in range(len(a)):
        l = 0
        r = 1
        while r < len(a):
            if a[l] > a[r]:
                count +=1
                a[l],a[r]=a[r],a[l]
            l +=1
            r +=1
    print("Array is sorted in " + str(count) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))
    
        


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
