#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    array = [0 for i in range(n + 1)]
    for q in queries:
        s, e, a = q[0] - 1, q[1], q[2]
        array[s] += a
        array[e] -= a
    s = 0
    answer = 0
    for i in array:
        s += i
        if s > answer:
            answer = s
    return answer
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

