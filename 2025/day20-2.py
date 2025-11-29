import sys
from collections import deque

D = [(-1,0), (0,1), (1,0), (0,-1)]

# parsing
X = [list(l.strip()) for l in open(sys.argv[1], 'r')]
nrow = len(X)
ncol = len(X[0])
assert all(len(row) == ncol for row in X)
# find the start and end
E = [(r,c) for r in range(nrow) for c in range(ncol) if X[r][c] == 'E']
assert len(E) == 1
E = E.pop()
S = [(r,c) for r in range(nrow) for c in range(ncol) if X[r][c] == 'S']
assert len(S) == 1
S = S.pop()

Q = deque([ (0, tuple(S)) ])
Seen = {tuple(S): 0}
min_step = None
while Q:
    step, (r,c) = Q.popleft()
    for dr,dc in D:
        # get the new coordinate
        nr = r+dr
        nc = c+dc
        # check if the new coordinate is valid
        if not 0<=nr<nrow or not 0<=nc<ncol or not nr<=nc<ncol-nr:
            continue
        # check if we can move to the new coordinate
        if X[nr][nc] not in 'TSE' or (dr < 0 and r % 2 != c % 2) or \
        (dr > 0 and r % 2 == c % 2):
            continue
        # check if the new coordinate has been seen
        step_next = step+1
        if (nr,nc) in Seen and Seen[(nr,nc)] <= step_next:
            continue
        Seen[(nr,nc)] = step_next
        # check if we have completed the journey
        if (nr,nc) == E:
            if min_step is None or step_next < min_step:
                min_step = step_next
            continue
        # continue the journey
        Q.append( (step_next, (nr,nc)) )
ans = min_step
print(ans)

