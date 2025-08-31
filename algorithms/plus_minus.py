#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    """
    Calculate and print the ratios of positive, negative, and zero values in an array.
    
    Args:
        arr: List of integers
    """
    n = len(arr)
    pos_count = 0
    neg_count = 0
    zero_count = 0
    
    for i in range(n):
        if arr[i] > 0:
            pos_count += 1
        elif arr[i] < 0:
            neg_count += 1
        else:
            zero_count += 1
    
    print(f"{pos_count/n:.6f}")
    print(f"{neg_count/n:.6f}")
    print(f"{zero_count/n:.6f}")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
