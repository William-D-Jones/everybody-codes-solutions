import sys
import re

# parsing
X = [line.strip() for line in open(sys.argv[1], 'r')]
Coord = []
for x in X:
    M = re.match(r'^x=([0-9]+) y=([0-9]+)', x)
    Coord.append( (int(M.group(1)), int(M.group(2))) )

# constraints
n_day = 100

ans = 0
for c,r in Coord:
    # calculate the number of elements on the snail's diagonal
    el = c+r-1
    # calculate the snail position after the indicated time has passed
    nc = (c-1 + n_day) % el + 1
    nr = (r-1 - n_day) % el + 1
    pos = nc + 100 * nr
    ans += pos
print(ans)

