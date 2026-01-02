import sys
import re

# parsing
X = [line.strip() for line in open(sys.argv[1], 'r')]
Coord = []
for x in X:
    M = re.match(r'^x=([0-9]+) y=([0-9]+)', x)
    Coord.append( (int(M.group(1)), int(M.group(2))) )

n_day = 0
while not all( (r-1 - n_day) % (c+r-1) == 0 for (c,r) in Coord ):
    n_day += 1
ans = n_day
print(ans)

