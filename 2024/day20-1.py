import sys
from collections import deque

D = [(0,1), (1,0), (0,-1), (-1,0)]

# parsing
X = [list(l.strip()) for l in open(sys.argv[1], 'r')]
nrow = len(X)
ncol = len(X[0])
assert all( len(row)==ncol for row in X )

# find the starting position
S = [(r,c) for r in range(nrow) for c in range(ncol) if X[r][c]=='S']
assert len(S)==1
S = S.pop()

# constraints
a_cliff = 1000
step_max = 100

Q = deque([(0, a_cliff, tuple(S), (0, 0))])
Seen = { (0, a_cliff, tuple(S), (0,0)) }
a_max = None
while Q:
    step, a, (r,c), (lr,lc) = Q.popleft()
    for dr,dc in D:
        # block returns to the previous coordinate
        if dr == -lr and dc == -lc:
            continue
        # get the new coordinate
        nr = r+dr
        nc = c+dc
        # check that the new coordinate is valid
        if not 0<=nr<nrow or not 0<=nc<ncol or X[nr][nc] in '#S':
            continue
        # get the new altitude
        if X[nr][nc] == '.':
            da = -1
        elif X[nr][nc] == '-':
            da = -2
        elif X[nr][nc] == '+':
            da = 1
        else:
            assert False
        a_next = a+da
        # check if the state has been seen
        step_next = step+1
        State = (a_next, (nr,nc))
        if State in Seen:
            continue
        Seen.add(State)
        # check if the journey is complete
        if step_next == step_max:
            if a_max is None or a_max < a_next:
                a_max = a_next
            continue
        # continue the journey
        Q.append( (step_next, a_next, (nr,nc), (dr,dc)) )
ans = a_max
print(ans)

