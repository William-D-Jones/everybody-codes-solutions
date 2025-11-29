import sys
from collections import deque
import math

D = [(-1,0), (0,1), (1,0), (0,-1)]

# parsing
X = [list(l.strip()) for l in open(sys.argv[1], 'r')]
nrow = len(X)
ncol = len(X[0])
assert all(len(row) == ncol for row in X)
# find the start
S = [(r,c) for r in range(nrow) for c in range(ncol) if X[r][c] == 'S']
assert len(S) == 1
S = S.pop()

# rotate the triangle counterclockwise
X1 = [['.' for c in range(ncol)] for r in range(nrow)]
for r in range(nrow):
    for c in range(ncol):
        if X[r][c] == '.':
            continue
        tr = (c-r)//2
        tc = ncol-1 - 2*r - math.ceil( (c-r)/2 )
        X1[r][c] = X[tr][tc]
X2 = [['.' for c in range(ncol)] for r in range(nrow)]
for r in range(nrow):
    for c in range(ncol):
        if X1[r][c] == '.':
            continue
        tr = (c-r)//2
        tc = ncol-1 - 2*r - math.ceil( (c-r)/2 )
        X2[r][c] = X1[tr][tc]
XR = [X, X2, X1]

# find the minimum path from S to E
Q = deque([])
Seen = {}
for n_wait in range(3):
    Q.append( (n_wait, tuple(S)) )
    Seen[(tuple(S), n_wait)] = n_wait
min_step = None
while Q:
    step, (r,c) = Q.popleft()
    if min_step is not None and step >= min_step:
        continue
    for dr,dc in D:
        # get the new coordinate
        nr = r+dr
        nc = c+dc
        # check if the new coordinate is valid
        if not 0<=nr<nrow or not 0<=nc<ncol or not nr<=nc<ncol-nr:
            continue
        # check if we can move to the new coordinate
        if (dr < 0 and r % 2 != c % 2) or (dr > 0 and r % 2 == c % 2):
            continue
        for n_wait in range(3):
            step_next = step + 1 + n_wait
            mod = step_next % 3
            # check if the new coordinate has been seen
            if ((nr,nc), mod) in Seen and Seen[((nr,nc), mod)] <= step_next:
                break
            Seen[((nr,nc), mod)] = step_next
            # check the item at the next coordinate
            loc = XR[mod][nr][nc]
            if loc not in 'TSE':
                break
            # check if we have completed the journey
            if loc == 'E':
                if min_step is None or step_next < min_step:
                    min_step = step_next
                break
            # continue the journey
            Q.append( (step_next, (nr,nc)) )
ans = min_step
print(ans)

