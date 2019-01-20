#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the nonDivisibleSubset function below.
#
from itertools import combinations
import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def nonDivisibleSubset(k, S):
    remainders = map(lambda i: i%k, S)
    answer = 0
    if k % 2 != 0:
        n = (k/2) + 1
    else:
        n = (k/2)
    for i in range(1, n):
        answer += max(remainders.count(i), remainders.count(k-i))
        print(answer)
    if 0 in remainders:
        answer += 1
    if k % 2 == 0 and k/2 in remainders:
        answer += 1
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    S = map(int, raw_input().rstrip().split())

    result = nonDivisibleSubset(k, S)

    fptr.write(str(result) + '\n')

    fptr.close()

