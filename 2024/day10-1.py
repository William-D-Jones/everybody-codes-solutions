import sys
from collections import deque

# parsing
X = [ list(l.strip()) for l in open(sys.argv[1], 'r') ]
nrow = len(X)
ncol = len(X[0])
Q = deque([(r,c) for r in range(nrow) for c in range(ncol) if X[r][c] == '.'])
S = sorted(list(Q))

while Q:
    xr,xc = Q.popleft()
    sr = set([X[xr][c] for c in range(ncol) if X[xr][c] not in '.*'])
    sc = set([X[r][xc] for r in range(nrow) if X[r][xc] not in '.*'])
    rune = sr & sc
    assert len(rune) <= 1
    if len(rune) == 1:
        rune = rune.pop()
        X[xr][xc] = rune
    else:
        Q.append( (xr,xc) )
ans = ''
for r,c in S:
    ans += X[r][c]
print(ans)

