import sys
import itertools

# parsing
X = [list(l.strip()) for l in open(sys.argv[1], 'r')]
nrow = len(X)
ncol = len(X[0])
assert all(len(row) == ncol for row in X)

# get the locations of the stars
S = set((r,c) for r in range(nrow) for c in range(ncol) if X[r][c] == '*')

# get the Manhattan distances between each pair of stars
M = {}
for (r0,c0),(r1,c1) in itertools.combinations(S, 2):
    m = abs(r0-r1)+abs(c0-c1)
    M[ tuple(sorted([(r0,c0),(r1,c1)])) ] = m

# connect the stars into a constellation
Grp = []
Orphan = set(S)
Leaf = [Orphan.pop()]
while Orphan:
    Poss = []
    for xr,xc in Orphan:
        for lr,lc in Leaf:
            Pair = tuple(sorted([(xr,xc), (lr,lc)]))
            m = M[Pair]
            Poss.append( (m,Pair) )
    Poss = sorted(Poss)[::-1]
    m,Pair = Poss.pop()
    nr,nc = Pair[0] if Pair[1] in Leaf else Pair[1]
    Grp.append(Pair)
    Leaf.append( (nr,nc) )
    Orphan.remove( (nr,nc) )

# compute the final answer
ans = len(S) + sum(M[Pair] for Pair in Grp)
print(ans)

