n = int(input())
minutes = list(map(int, input().split()))
sumY = 0
sumM = 0

for minute in minutes:
    y = 10 * (minute // 30 + 1)
    sumY += y
    m = 15 * (minute // 60 + 1)
    sumM += m

if y > m:
    print('M', sumM)
elif y < m:
    print('Y', sumY)
else:
    print('Y', 'M', sumY)