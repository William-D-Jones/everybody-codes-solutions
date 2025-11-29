import sys

# parsing
X = [list(l.strip()) for l in open(sys.argv[1], 'r')]
nrow = len(X)
ncol = len(X[0])
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

# constraints
R = 10

ans = 0
for r in range(nrow):
    for c in range(ncol):
        if (r,c) == Cen:
            continue
        if (Cen[1] - c) ** 2 + (Cen[0] - r) ** 2 <= R ** 2:
            ans += Vol[r][c]
print(ans)

