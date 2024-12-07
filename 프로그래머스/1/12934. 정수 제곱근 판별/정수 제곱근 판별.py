import math

def solution(n):
    x = int(math.sqrt(n))
    if (x * x == n):
        return (x+1)*(x+1)
    return -1