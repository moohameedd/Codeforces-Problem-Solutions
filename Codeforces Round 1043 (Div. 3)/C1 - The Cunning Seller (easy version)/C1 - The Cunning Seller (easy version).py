# Code by Mohamed

t = int (input () )
for _ in range (t) :
    n = int( input () )
    s=0
    while n>0:
        x=0
        while 3**(x+1)<=n:
            x=x+1
        nb=n//(3**x)
        s=s+nb*((3**(x+1)+x*(3**(x-1))))
        n=n%(3**x)
    print(int(s))

