import sys

# parsing
X = list(open(sys.argv[1], 'r').read().strip())

# part 1
ans = 0
for x in X:
    match x:
        case 'A':
            pass
        case 'B':
            ans += 1
        case 'C':
            ans += 3
print(ans)

