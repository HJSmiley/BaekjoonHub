n = int(input())
dict = {'D': 0, 'P': 0}

for _ in range(n):
    win = input()
    if win == 'D':
        dict['D'] += 1
    else:
        dict['P'] += 1
    
    s = dict['D'] - dict['P']
    if s == 2 or s == -2:
        break

print(dict['D'], ':', dict['P'], sep='')