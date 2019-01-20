#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the climbingLeaderboard function below.
#
def climbingLeaderboard(scores, alice):
    scores = sorted(set(scores), reverse=True)
    l = len(scores)
    alice = sorted(alice)
    answer = []
    for a in alice:
        while l > 0 and (a >= scores[l-1]):
            l -= 1
        answer.append(l + 1)
    return answer
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(raw_input())

    scores = map(int, raw_input().rstrip().split())

    alice_count = int(raw_input())

    alice = map(int, raw_input().rstrip().split())

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

