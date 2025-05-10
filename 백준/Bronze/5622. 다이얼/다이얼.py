s = input()
nums = []

for c in s:
    asc = ord(c)
    num = 0

    if 65 <= asc <= 67:
        num = 2
    elif 68 <= asc <= 70:
        num = 3
    elif 71 <= asc <= 73:
        num = 4
    elif 74 <= asc <= 76:
        num = 5
    elif 77 <= asc <= 79:
        num = 6
    elif 80 <= asc <= 83:
        num = 7
    elif 84 <= asc <= 86:
        num = 8
    elif 87 <= asc <= 90:
        num = 9
    
    nums.append(num)

print(sum(nums) + len(nums))