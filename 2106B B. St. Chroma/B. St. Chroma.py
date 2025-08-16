# Code by Mohamed

numbers = [i for i in range(200000)]

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())

    if x > n or (n == 1 and x == 0):
        print(0)
    else:
        if x == n:
            print(*numbers[:x])
        else:
            perm = numbers[:x] + numbers[x+1:n]
            perm.append(x)
            print(*perm)
