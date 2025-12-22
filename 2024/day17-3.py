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
Orphan = set()
for (r0,c0),(r1,c1) in itertools.combinations(S, 2):
    m = abs(r0-r1)+abs(c0-c1)
    if m<6:
        M[ tuple(sorted([(r0,c0),(r1,c1)])) ] = m
        Orphan.add( (r0,c0) )
        Orphan.add( (r1,c1) )

# connect the stars into a constellation
Grp = [[]]
Leaf = set([Orphan.pop()])
MO = dict(M)
while Orphan:
    Poss = []
    for lr,lc in set(Leaf):
        p0 = len(Poss)
        for Pair,m in MO.items():
            if ( (lr,lc)==Pair[0] and Pair[1] in Orphan ) or \
            ( (lr,lc)==Pair[1] and Pair[0] in Orphan ):
                Poss.append( (m,Pair) )
        p1 = len(Poss)
        if p0==p1:
            Leaf.remove( (lr,lc) )
    if not Poss:
        Grp.append([])
        Leaf = set([Orphan.pop()])
        continue
    Poss = sorted(Poss)[::-1]
    m,Pair = Poss.pop()
    nr,nc = Pair[0] if Pair[1] in Leaf else Pair[1]
    Grp[-1].append(Pair)
    Leaf.add( (nr,nc) )
    Orphan.remove( (nr,nc) )
    MO.pop(Pair)

# compute the final answer
Sz = []
for grp in Grp:
    sz = len(grp)+1 + sum(M[Pair] for Pair in grp)
    Sz.append(sz)
Sz = sorted(Sz)
ans = Sz[-1] * Sz[-2] * Sz[-3]
print(ans)

