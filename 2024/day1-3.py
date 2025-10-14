import sys

# parsing
X = list(open(sys.argv[1], 'r').read().strip())

# part 3
ans = 0
for i in range(len(X)//3):
    Monsters = X[ 3*i : 3*i+3 ]
    for monster in Monsters:
        match monster:
            case 'A':
                pass
            case 'B':
                ans += 1
            case 'C':
                ans += 3
            case 'D':
                ans += 5
            case 'x':
                pass
    if Monsters.count('x') == 1:
        ans += 2
    elif Monsters.count('x') == 0:
        ans += 6
print(ans)

