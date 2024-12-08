def solution(x):
    nums = 0
    for num in list(str(x)):
        nums += int(num)
    if (x % nums == 0):
        return True
    return False