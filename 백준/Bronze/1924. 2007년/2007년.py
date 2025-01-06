dates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

x, y = map(int, input().split())
Date = 0

for i in range(x-1):
    Date = Date + dates[i]
Date = (Date + y) % 7

print(days[Date])