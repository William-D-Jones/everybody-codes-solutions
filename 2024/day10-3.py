import sys

A = ord('A')

def solve_grid(Grid):
    # get the size of the grid
    nrow = len(Grid)
    ncol = len(Grid[0])
    # setup a queue of coordinates to fill
    Q = [(r,c) for r in range(nrow) for c in range(ncol) if \
    Grid[r][c] in '.']
    # solve coordinates
    while True:
        Q_Next = []
        for xr,xc in Q:
            # get the unique characters in the current row/column
            sr = set([Grid[xr][c] for c in range(ncol) if \
            Grid[xr][c] not in '.*?'])
            sc = set([Grid[r][xc] for r in range(nrow) if \
            Grid[r][xc] not in '.*?'])
            # find any characters in common between the current row/column
            rune = sr & sc
            if len(rune) == 1:
                rune = rune.pop()
                Grid[xr][xc] = rune
            elif len(rune) == 0:
                # collect all the non-empty characters in the current row/column
                Char = [char for char in Grid[xr] if char != '*'] + \
                [Grid[r][xc] for r in range(nrow) if Grid[r][xc] != '*']
                # identify non-duplicate characters
                char_uni = [char for char in Char if \
                Char.count(char) == 1 and char not in '.?']
                # check if we can fill in a . and a ? using the uniqueness rule
                if Char.count('.') == 2 and Char.count('?') == 1 and \
                len(char_uni) == 1:
                    char_uni = char_uni.pop()
                    for r in range(nrow):
                        if Grid[r][xc] in '.?':
                            Grid[r][xc] = char_uni
                    for c in range(ncol):
                        if Grid[xr][c] in '.?':
                            Grid[xr][c] = char_uni
                else:
                    Q_Next.append( (xr,xc) )
            else:
                pass
        # check if we have made any progress
        if len(Q_Next) == len(Q):
            break
        else:
            Q = Q_Next
    return Grid

# parsing
X = [ list(l.strip()) for l in open(sys.argv[1], 'r') ]
nrow = len(X)
ncol = len(X[0])

# constraints
sz = 8
sh = 2

# determine the number of grids
ngrow = (nrow - sh) // (sz - sh)
ngcol = (ncol - sh) // (sz - sh)

# solve coordinates
Q = [(gr,gc) for gr in range(ngrow) for gc in range(ngcol)]
ans = 0
while True:
    Q_Next = []
    for gr,gc in Q:
        # extract the current grid
        rng_r = range( (sz-sh)*gr, (sz-sh)*gr + sz)
        rng_c = range( (sz-sh)*gc, (sz-sh)*gc + sz)
        Grid = [ [ X[r][c] for c in rng_c ] for r in rng_r ]
        # solve the grid
        Grid = solve_grid(Grid)
        # extract the runic word
        word = ''.join([''.join(Grid[r][sh:sz-sh]) for r in range(sh,sz-sh)])
        if '.' in word:
            Q_Next.append( (gr,gc) )
        else:
            for i,char in enumerate(word):
                ans += (i+1) * (ord(char) - A + 1)
        # use the findings to adjust the input
        for r in range(sz):
            X[ (sz-sh)*gr + r ][ (sz-sh)*gc : (sz-sh)*gc + sz ] = Grid[r]
    # check if we have made any progress
    if len(Q_Next) == len(Q):
        break
    else:
        Q = Q_Next
print(ans)

