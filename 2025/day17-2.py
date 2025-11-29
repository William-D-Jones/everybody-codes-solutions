import sys
import math

# parsing
X = [list(l.strip()) for l in open(sys.argv[1], 'r')]
nrow = len(X)
ncol = len(X[0])
assert nrow == ncol
assert all(len(row) == ncol for row in X)
Vol = list(X)
Cen = []
for r in range(nrow):
    for c in range(ncol):
        if Vol[r][c] == '@':
            Cen.append( (r,c) )
        else:
            Vol[r][c] = int(Vol[r][c])
assert len(Cen) == 1
Cen = Cen.pop()

Dest = {}
Tot = {}
for R in range(1, ncol // 2):
    dest = set()
    for r in range(nrow):
        for c in range(ncol):
            if (r,c) == Cen:
                continue
            if (Cen[1] - c) ** 2 + (Cen[0] - r) ** 2 <= R ** 2:
                dest.add( (r,c) )
    for m in range(1, R):
        dest -= Dest[R-m]
    Dest[R] = dest
    Tot[R] = sum(Vol[r][c] for (r,c) in Dest[R])

ans = math.prod(sorted((tot,R) for R,tot in Tot.items())[-1])
print(ans)

