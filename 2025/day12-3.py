import sys
from collections import deque

D = [(0,1), (1,0), (0,-1), (-1,0)]

# parsing
X = [list(map(int,list(l.strip()))) for l in open(sys.argv[1], 'r')]
nrow = len(X)
ncol = len(X[0])
assert all(len(row) == ncol for row in X)

# constraints
n_fire = 3

# start one fire from each coordinate
F1 = {}
for sr in range(nrow):
    for sc in range(ncol):
        Fire = set( [(sr,sc)] )
        Q = deque( [(sr,sc)] )
        while Q:
            r,c = Q.popleft()
            sz = X[r][c]
            for dr,dc in D:
                nr = r+dr
                nc = c+dc
                if not (0<=nr<nrow and 0<=nc<ncol) or (nr,nc) in Fire or \
                X[nr][nc] > sz:
                    continue
                if (nr,nc) in F1.keys():
                    Fire |= F1[(nr,nc)]
                    continue
                Fire.add( (nr,nc) )
                Q.append( (nr,nc) )
        F1[(sr,sc)] = Fire

# get the best burn that can be accomplished with the given starting barrels
Burned = set()
for ix_fire in range(n_fire):
    max_burn = 0
    for sr in range(nrow):
        for sc in range(ncol):
            Burned_Next = Burned | F1[(sr,sc)]
            if len(Burned_Next) > max_burn:
                max_burn = len(Burned_Next)
                max_burned = F1[(sr,sc)]
    Burned |= max_burned
ans = len(Burned)
print(ans)

