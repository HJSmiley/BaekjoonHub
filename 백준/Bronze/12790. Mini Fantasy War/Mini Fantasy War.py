t = int(input())

for _ in range(t):
    b_hp, b_mp, b_a, b_d, a_hp, a_mp, a_a, a_d = map(int, input().split())
    hp = b_hp + a_hp if b_hp + a_hp >= 1 else 1
    mp = b_mp + a_mp if b_mp + a_mp >= 1 else 1
    a = b_a + a_a if b_a + a_a >= 0 else 0
    d = b_d + a_d
    print(1 * hp + 5 * mp + 2 * a + 2 * d)