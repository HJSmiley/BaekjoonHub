dic = {"w": "chunbae", "b": "nabi", "g": "yeongcheol"}

for _ in range(15):
    pixels = input()
    for pixel in pixels:
        if pixel in dic:
            print(dic[pixel])
            exit()