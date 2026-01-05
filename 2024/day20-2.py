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
a_cliff = 10000
Item_Name = ['A', 'B', 'C']

# get the locations of the items
Item_Coord = {name: [] for name in Item_Name}
for r in range(nrow):
    for c in range(ncol):
        if X[r][c] in Item_Coord:
            Item_Coord[ X[r][c] ].append( (r,c) )
# we assume that all items occur exactly once in the grid
assert all(len(Coord)==1 for Coord in Item_Coord.values())
Get = [Item_Coord[name][0] for name in Item_Name]

Q = deque([(0, a_cliff, tuple(S), (0, 0), -1)])
Seen = { ((0,0), -1): (0, a_cliff) }
step_min = None
last = 0
while Q:
    step, a, (r,c), (lr,lc), i = Q.popleft()
    # check if we have stepped too far
    if step_min is not None and step >= step_min:
        continue
    for dr,dc in D:
        # block returns to the previous coordinate
        if dr == -lr and dc == -lc:
            continue
        # get the new coordinate
        nr = r+dr
        nc = c+dc
        # check that the new coordinate is valid
        if not 0<=nr<nrow or not 0<=nc<ncol or X[nr][nc] in '#':
            continue
        # check if the journey is complete
        step_next = step+1
        if nr==S[0] and nc==S[1]:
            if a > a_cliff and i == len(Get)-1:
                if step_min is None or step_min > step_next:
                    step_min = step_next
            continue
        # check if we can gather any item present
        if (nr,nc) in Get:
            if i<len(Get)-1 and Get[i+1]==(nr,nc):
                i_next = i+1
            else:
                continue
        else:
            i_next = i
        # get the new altitude
        if X[nr][nc] == '.' or (nr,nc) in Get:
            da = -1
        elif X[nr][nc] == '-':
            da = -2
        elif X[nr][nc] == '+':
            da = 1
        else:
            assert False
        a_next = a+da
        # check if the state has been seen
        State = ((nr,nc), i_next)
        if State in Seen and \
        Seen[State][0]<=step_next and Seen[State][1]>=a_next:
            continue
        Seen[State] = (step_next, a_next)
        # continue the journey
        Q.append( (step_next, a_next, (nr,nc), (dr,dc), i_next) )
ans = step_min
print(ans)

