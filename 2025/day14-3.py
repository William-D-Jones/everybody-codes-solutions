import sys

D = [(-1,1), (1,1), (1,-1), (-1,-1)]

# parsing
X = [list(l.strip()) for l in open(sys.argv[1], 'r')]
nrow_check = len(X)
ncol_check = len(X[0])
assert all(len(row) == ncol_check for row in X)

# constraints
n_rnd = 1000000000
nrow = 34
ncol = 34

# calculate start and end points for checking the grid
start_row = (nrow - nrow_check) // 2
start_col = (ncol - ncol_check) // 2

# simulate grids until we encounter a repeat
Grid = [['.' for c in range(ncol)] for r in range(nrow)]
Seen = []
Match = {}
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
    # check if the grid is a match to the check grid
    if all(Grid[start_row + r][start_col + c] == \
    X[r][c] for r in range(nrow_check) for c in range(ncol_check)):
        Match[rnd] = \
        sum(1 for r in range(nrow) for c in range(ncol) if Grid[r][c] == '#')
    # check if the grid has been seen before
    State = tuple(tuple(row) for row in Grid)
    if State in Seen:
        break
    else:
        Seen.append(State)

# identify how the grid repeats
rnd_rep = rnd
rnd_orig = Seen.index(State)

# calculate the final answer
# add the grids that occur before the first repeat
ans = sum(Match[rnd] for rnd in Match.keys() if not rnd_orig<=rnd<rnd_rep)
# add the grids corresponding to the number of complete repeats that occur
n_rep = (n_rnd - rnd_orig) // (rnd_rep - rnd_orig)
ans += sum(Match[rnd] * n_rep for rnd in Match.keys() if rnd_orig<=rnd<rnd_rep)
# add the grids that occur after the final complete repeat
n_rnd_end = n_rnd - (rnd_orig + n_rep * (rnd_rep - rnd_orig))
ans += sum(Match[rnd] for rnd in Match.keys() if 0<=rnd-rnd_orig<n_rnd_end)
print(ans)

