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
# find the sheep
Sheep = deque(\
[((r,c),0) for r in range(nrow) for c in range(ncol) if X[r][c] == 'S']\
)

# constraints
n_round = 20

# find the possible positions of the dragon and how many steps to get there
Seen = set()
Step = {}
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
            Step[ (nr,nc) ] = n_step+1
            # continue moving if space is available
            if n_step + 1 < n_round:
                Q.append( ((nr,nc), n_step+1) )

# simulate the sheep
ans = 0
while Sheep:
    (r,c), n_step = Sheep.popleft()
    # check if the the sheep is on a dragon square
    if (r,c) in Step and Step[ (r,c) ] <= n_step + 1 and \
    Step[ (r,c) ] % 2 != n_step % 2 and X[r][c] != '#':
        ans += 1
        continue
    # move the sheep
    r += 1
    n_step += 1
    # check if the sheep escaped
    if r >= nrow:
        continue
    # check if the sheep moved to a dragon square
    if (r,c) in Step and Step[ (r,c) ] <= n_step and \
    Step[ (r,c) ] % 2 == n_step % 2 and X[r][c] != '#':
        ans += 1
        continue
    # if the sheep survived, continue the sheep
    if n_step < n_round:
        Sheep.append( ((r,c), n_step) )
print(ans)

