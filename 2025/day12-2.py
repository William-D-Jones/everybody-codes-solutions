import sys
from collections import deque

D = [(0,1), (1,0), (0,-1), (-1,0)]

# parsing
X = [list(map(int,list(l.strip()))) for l in open(sys.argv[1], 'r')]
nrow = len(X)
ncol = len(X[0])
assert all(len(row) == ncol for row in X)

# constraints
S = [(0,0), (nrow-1,ncol-1)]

Fire = set(S)
Q = deque(S)
while Q:
    r,c = Q.popleft()
    sz = X[r][c]
    for dr,dc in D:
        nr = r+dr
        nc = c+dc
        if not (0<=nr<nrow and 0<=nc<ncol) or (nr,nc) in Fire or \
        X[nr][nc] > sz:
            continue
        Fire.add( (nr,nc) )
        Q.append( (nr,nc) )
ans = len(Fire)
print(ans)

