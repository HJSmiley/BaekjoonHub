day = int(input())
cars = list(map(int, input().split()))
result = 0

for car in cars:
    if car == day:
        result += 1

print(result)