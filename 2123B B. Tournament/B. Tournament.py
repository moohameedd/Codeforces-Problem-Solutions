# Code by Mohamed

t = int(input())
for _ in range(t):
    n, j, k = map(int, input().split())
    a = list(map(int, input().split()))
    player = a[j-1]

    mx = max(a)  

    if k > 1 or player == mx:
        print("YES")
    else:
        print("NO")
