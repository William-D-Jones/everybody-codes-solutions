import sys
from copy import deepcopy

D = [(-1,1), (1,1), (1,-1), (-1,-1)]

# parsing
X = [list(l.strip()) for l in open(sys.argv[1], 'r')]
nrow = len(X)
ncol = len(X[0])
assert all(len(row) == ncol for row in X)

# constraints
n_rnd = 2025

ans = 0
Grid = deepcopy(X)
for rnd in range(n_rnd):
    Grid_Next = [['' for c in range(ncol)] for r in range(nrow)]
    for r in range(nrow):
        for c in range(ncol):
            num_active = 0
            for dr,dc in D:
                nr = r+dr
                nc = c+dc
                if not (0<=nr<nrow and 0<=nc<ncol):
                    continue
                if Grid[nr][nc] == '#':
                    num_active += 1
            if Grid[r][c] == '#':
                if num_active % 2 != 0:
                    Grid_Next[r][c] = '#'
                else:
                    Grid_Next[r][c] = '.'
            elif Grid[r][c] == '.':
                if num_active % 2 == 0:
                    Grid_Next[r][c] = '#'
                else:
                    Grid_Next[r][c] = '.'
            else:
                assert False
    Grid = Grid_Next
    ans += sum(1 for r in range(nrow) for c in range(ncol) if Grid[r][c] == '#')
print(ans)

