n, b = map(str, input().split())
b = int(b)
ans = 0
chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mod_dict = {chars[j]: j for j in range(len(chars))}

for i, c in enumerate(n[::-1]):
    ans += (b**i) * mod_dict[c]

print(ans)