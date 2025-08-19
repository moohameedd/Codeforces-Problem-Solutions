# Code by Mohamed

t = int(input())
for _ in range (t):
    n,k=map ( int , input() . split() )
    l=[]
    for i in range(n):
        a=list(map ( int , input() . split() ))
        l.append(a)

    l=sorted(l,key=lambda x :x[0])
    for i in range(n):
        if l[i][0]<=k<=l[i][1] and k<=l[i][2]:
            k=l[i][2]
    print(k)