#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    diagonal1 = 0
    diagonal2 = 0
    for i in range(len(arr[0])):
        diagonal1 += arr[i][i]
        diagonal2 += arr[i][len(arr[0]) - i - 1]

    difference = diagonal1 - diagonal2
    if difference >= 0:
        return difference
    else:
        return -1*difference

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

