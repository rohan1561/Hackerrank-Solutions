#!/bin/python

import sys

def extraLongFactorials(n):
    return reduce(lambda x, y: x*y, range(1, n+1))

if __name__ == "__main__":
    n = int(raw_input().strip())
    print(extraLongFactorials(n))

