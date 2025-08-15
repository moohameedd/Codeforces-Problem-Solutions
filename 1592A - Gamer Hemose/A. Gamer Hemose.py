# Code by Mohamed
t = int(input())
for _ in range(t):
    n, h = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    strongest = a[0]
    second_strongest = a[1]
    cycle_damage = strongest + second_strongest
    full_cycles = h // cycle_damage
    moves = full_cycles * 2
    reste = h % cycle_damage
    if reste == 0:
        pass  
    elif reste <= strongest:
        moves += 1
    else:
        moves += 2

    print(moves)
