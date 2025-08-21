# Code by Mohamed
t=[]
for i in range(100):
    t.append(i*i)
def bn_search(x, t):
    l=0
    r=99
    res = -1
    while l <= r:
        mid = (l + r) // 2
        if t[mid] == x:
            res = mid
            break
        elif t[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    if res == -1:
        print(-1)
    elif res==0:
        print("0 0")
    else:
        print(f"{res-1} 1")






j=int(input())
for _ in range(j):
    s=input()
    bn_search(int(s),t)
