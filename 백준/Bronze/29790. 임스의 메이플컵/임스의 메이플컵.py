N, U, L = map(int, input().split())

if N < 1000:
    print('Bad')
else:
    if U >= 8000 or L >= 260:
        print('Very Good')
    else:
        print('Good')