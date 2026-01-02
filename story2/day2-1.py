import sys

# parsing
Balloon = list(open(sys.argv[1], 'r').read().strip())

# constraints
Bolt = ['R', 'G', 'B']

pnt = 0
ans = 0
while Balloon:
    ans += 1
    while Balloon and Balloon.pop(0) == Bolt[pnt]:
        continue
    pnt = (pnt + 1) % len(Bolt)
print(ans)

