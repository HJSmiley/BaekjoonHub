from math import sqrt
from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = set()
    n = len(numbers)
    numbers = list(map(int, numbers))
    tmp = []
    
    numbers.sort()
    for i in range(1, n+1):
        tmp.append(set(permutations(numbers, i)))
        
    for i in tmp:
        for j in i:
            j = int(''.join([str(item) for item in j]))
            if is_prime(j):
                answer.add(j)

    return len(answer)