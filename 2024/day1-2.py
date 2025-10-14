import sys

# parsing
X = list(open(sys.argv[1], 'r').read().strip())

# part 2
ans = 0
for i in range(len(X)//2):
    Monsters = X[ 2*i : 2*i+2 ]
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
    if Monsters.count('x') == 0:
        ans += 2
print(ans)

