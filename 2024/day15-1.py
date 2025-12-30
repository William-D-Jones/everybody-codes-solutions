import sys
from collections import deque

D = [(0,1), (1,0), (0,-1), (-1,0)]
A = ord('A')
Z = ord('Z')

# parsing
X = [list(l.strip()) for l in open(sys.argv[1], 'r')]
nrow = len(X)
ncol = len(X[0])
assert all(len(row) == ncol for row in X)

# find the starting position
S = [(0,c) for c in range(ncol) if X[0][c] == '.']
assert len(S) == 1
S = S.pop()

# items to be collected
Col = set(['H'])

min_step = None
Seen = set([(S, '')])
Q = deque([[S, set(), 0]])
while Q:
    (r,c), Herb, step = Q.popleft()
    for dr,dc in D:
        # compute the new coordinate and check if it is valid
        nr = r+dr
        nc = c+dc
        if not 0<=nr<nrow or not 0<=nc<ncol or X[nr][nc] == '#':
            continue
        # pick up an herb if one is available
        Herb_Next = set(Herb)
        if A<=ord(X[nr][nc])<=Z:
            Herb_Next.add(X[nr][nc])
        # skip states that have been seen before
        State = ( (nr,nc), ''.join(sorted(list(Herb_Next))) )
        if State in Seen:
            continue
        Seen.add( State )
        # check if we have finished the journey
        step_next = step + 1
        if (nr,nc) == S and Herb_Next == Col:
            if min_step is None or min_step > step_next:
                min_step = step_next
        else:
            Q.append( [(nr,nc), Herb_Next, step_next] )
ans = min_step
print(ans)

