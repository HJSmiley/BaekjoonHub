arr = list(map(str, input()))

while arr[-2:] == '()':
    arr = arr[:-2]

rods = 0
answer = 0
i = 0

while i < len(arr):
    if arr[i] == '(':
        if arr[i + 1] == ')':
            answer += rods
            i += 2
            continue
        else:
            rods += 1
    elif arr[i] == ')':
        rods -= 1
        answer += 1
    i += 1

print(answer)