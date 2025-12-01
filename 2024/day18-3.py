import sys
from collections import deque

D = [(0,1), (1,0), (0,-1), (-1,0)]

# parsing
X = [list(l.strip()) for l in open(sys.argv[1], 'r')]
nrow = len(X)
ncol = len(X[0])
assert all(len(row)==ncol for row in X)

# find the possible starting coordinates
S = set([(r,c) for r in range(nrow) for c in range(ncol) if X[r][c] == '.'])

# find the palms
Palm = set([(r,c) for r in range(nrow) for c in range(ncol) if X[r][c] == 'P'])

# for each palm, find the shortest path to each candidate well
Path = {}
for p in Palm:
    Seen = set([p])
    Front = [p]
    t = 0
    while Front:
        Front_Next = []
        t += 1
        while Front:
            r,c = Front.pop()
            for dr,dc in D:
                nr = r+dr
                nc = c+dc
                # check if the new coordinate is valid and unseen
                if not (0<=nr<nrow and 0<=nc<ncol) or X[nr][nc] not in '.P' or \
                (nr,nc) in Seen:
                    continue
                Seen.add( (nr,nc) )
                Front_Next.append( (nr,nc) )
                # check if we have found a candidate well
                if X[nr][nc] == '.':
                    Path[ ((nr,nc), p) ] = t
        Front = Front_Next

# determine the minimum sum of the paths to each palm
ans = min(sum(Path[ (s,p) ] for p in Palm) for s in S)
print(ans)

