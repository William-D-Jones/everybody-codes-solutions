import sys

D = [(0,1), (1,0), (0,-1), (-1,0)]

# parsing
X = [list(l.strip()) for l in open(sys.argv[1], 'r')]
nrow = len(X)
ncol = len(X[0])
assert all(len(row)==ncol for row in X)

# find the starting position
S = [(r,c) for r in range(nrow) for c in range(ncol) if \
X[r][c] == '.' and (r==0 or r==nrow-1 or c==0 or c==ncol-1)]
assert len(S) == 1
S = S.pop()

# find the palms
Palm = set([(r,c) for r in range(nrow) for c in range(ncol) if X[r][c] == 'P'])

# irrigate the farm
Seen = set([S])
Front = [S]
Found = set()
t = 0
while Found != Palm and Front:
    Front_Next = []
    while Front:
        r,c = Front.pop()
        for dr,dc in D:
            nr = r+dr
            nc = c+dc
            # check if the new coordinate is valid and unseen
            if not (0<=nr<nrow and 0<=nc<ncol) or X[nr][nc] not in '.P' or \
            (nr,nc) in Seen:
                continue
            Seen.add( (r,c) )
            # check if we have found a palm
            if X[nr][nc] == 'P':
                Found.add( (nr,nc) )
            Front_Next.append( (nr,nc) )
    Front = Front_Next
    t += 1
ans = t
print(ans)

