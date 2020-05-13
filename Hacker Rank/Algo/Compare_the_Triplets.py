import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.


def compareTriplets(a, b):
    score = []
    alice = 0
    bob = 0
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] > b[i]:
                alice = alice + 1
            elif a[i] < b[i]:
                bob = bob + 1
            else:
                continue
    else:
        print("The length of both the list are unequal. Please try again.")

    score = [alice, bob]
    return score

'''if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
'''
a = [1,5,7]
b = [7,5,1]
result = compareTriplets(a, b)
print(result)