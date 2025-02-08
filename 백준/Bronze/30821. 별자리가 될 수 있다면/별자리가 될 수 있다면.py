from math import factorial
n = int(input())
print(factorial(n) // (factorial(n-5) * factorial(5)))