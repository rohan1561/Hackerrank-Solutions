#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    count = 0
    directions = [[1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1]]
    for d in directions:
        x = d[0]
        y = d[1]
        l = r_q
        m = c_q
        while True:
            l += x
            m += y
            if l > n or m > n or l < 1 or m < 1:
                break
            #elif (str(l) + '-' + str(m)) in obstacles:
            elif (l, m) in obstacles:
                break
            count += 1
    return count
    
if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = set()

    for _ in range(k):
        a, b = (input().rstrip().split(' '))
        obstacles.add((int(a), int(b)))
        #obstacles[str(a) + '-' + str(b)] = -1
    
    result = queensAttack(n, k, r_q, c_q, obstacles)
    
    fptr.write(str(result) + '\n')

    fptr.close()


    

