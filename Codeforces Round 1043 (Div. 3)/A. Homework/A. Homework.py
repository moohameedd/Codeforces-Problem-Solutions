# Code by Mohamed


t = int (input () )
for _ in range (t) :
    n = int(input())
    a = input ()
    m = int( input () )
    b = input()
    c = input()
    for i in range (m):
        if c [i] == "D":
            a = a + b[i]
        else:
            a = b[i] + a
    print(a)
