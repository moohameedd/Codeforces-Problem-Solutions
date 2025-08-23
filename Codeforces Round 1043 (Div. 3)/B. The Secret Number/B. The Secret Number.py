# Code by Mohamed

t = int(input())
for _ in range(t):
    n = int(input())
    l = []
    k = 1
    while (10**k) < n:
        div = 1 + 10**k
        if n % div == 0:
            x = n // div
            if x > 0 and x < n:
                l.append(x)
        k += 1
    if not l:
        print(0)
    else:
        print(len(l))
        print(" ".join(map(str, sorted(l))))