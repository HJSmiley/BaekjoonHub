from functools import cmp_to_key

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))
    answer = ''.join(numbers)
    return "0" if int(answer) == 0 else answer