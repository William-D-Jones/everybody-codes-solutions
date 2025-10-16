import sys
from collections import deque, defaultdict

D = [ (0,1), (1,0), (0,-1), (-1,0) ]

# parsing
X = [ list(l.strip()) for l in open(sys.argv[1], 'r') ]
nrow = len(X)
ncol = len(X[0])

# part 1
Q = deque( [(r,c) for r in range(nrow) for c in range(ncol) if X[r][c] == '#'] )
N = defaultdict(int)
while Q:
    r,c = Q.popleft()
    n = N[(r,c)]
    if all(N[(r+dr,c+dc)] >= n for dr,dc in D):
        N[(r,c)] = n+1
        Q.append( (r,c) )
ans = sum(N.values())
print(ans)

