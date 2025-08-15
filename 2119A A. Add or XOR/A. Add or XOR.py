# Code by Mohamed
t = int(input())

for _ in range(t):
    a, b, cost_add, cost_xor = map(int, input().split())

    if a > b:
        if a ^ 1 == b:
            print(cost_xor)
        else:
            print(-1)
    else:
        diff = b - a
        xor_count = (b + 1) // 2 - (a + 1) // 2

        cost_only_add = diff * cost_add
        cost_mix = xor_count * cost_xor + (diff - xor_count) * cost_add

        print(min(cost_only_add, cost_mix))
