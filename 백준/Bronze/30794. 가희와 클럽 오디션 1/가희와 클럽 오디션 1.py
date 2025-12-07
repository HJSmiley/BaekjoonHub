lv, de = input().split()
lv = int(lv)

if de == "miss":
    print(0)
elif de == "bad":
    print(lv * 200)
elif de == "cool":
    print(lv * 400)
elif de == "great":
    print(lv * 600)
else:
    print(lv * 1000)