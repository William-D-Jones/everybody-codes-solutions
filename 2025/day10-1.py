import sys
from collections import deque

D = [(0,1), (1,0), (0,-1), (-1,0)]

# parsing
X = [list(l.strip()) for l in open(sys.argv[1], 'r')]
nrow = len(X)
ncol = len(X[0])
assert all(len(row) == ncol for row in X)
# find the dragon
Dragon = [(r,c) for r in range(nrow) for c in range(ncol) if X[r][c] == 'D']
assert len(Dragon) == 1
Dragon = Dragon.pop()

# constraints
n_move = 4

S = set()
Seen = set()
Q = deque([(tuple(Dragon), 0)])
while Q:
    (qr,qc), n_step = Q.popleft()
    for dxi,(dr0,dc0) in enumerate(D):
        for perp in (1,3):
            dr1,dc1 = D[(dxi+perp) % len(D)]
            # get the new position of the dragon
            nr = qr + dr0 * 2 + dr1
            nc = qc + dc0 * 2 + dc1
            # check that the new position is valid
            if not 0 <= nr < nrow or not 0 <= nc < ncol or (nr,nc) in Seen:
                continue
            Seen.add( (nr,nc) )
            # check if we have found a sheep
            if X[nr][nc] == 'S':
                S.add( (nr,nc) )
            # continue moving if space is available
            if n_step + 1 < n_move:
                Q.append( ((nr,nc), n_step+1) )
ans = len(S)
print(ans)

