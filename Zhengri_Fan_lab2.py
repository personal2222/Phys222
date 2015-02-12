import numpy as np
import pylab
import scipy
import sys

sys.setrecursionlimit(10**6)

def catlanNum(n):
    assert n >= 1, "invalid input"
    if n == 1:
        return 1
    else:
        n -=1
        return catlanNum(n)*(4*n+2)/(n+2)
def catlanNum(n):
    assert n >= 1, "invalid input"
    result = 1
    resultList = []
    for i in range(0,n):
        result = (4*i+2)/(i+2) * result
        resultList += [result]
    print(resultList)
