# Code by Mohamed
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    nb=0
    for i in range(n):
        if s[i]=="0":
            nb=nb+1
        nb=nb+(s[:i]+s[i+1:]).count('1')
    print(nb)