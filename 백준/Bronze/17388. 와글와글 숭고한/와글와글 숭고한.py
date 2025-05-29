s, k, h = map(int, input().split())

if s+k+h>=100:
    print('OK')
else:
    if s > k:
        if k > h:
            print('Hanyang')
        else:
            print('Korea')
    else:
        if s > h:
            print('Hanyang')
        else:
            print('Soongsil')