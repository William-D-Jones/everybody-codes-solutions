import sys
from collections import deque

A = ord('A')

def get_word(Sample):
    # get the size of the sample grid
    nrow = len(Sample)
    ncol = len(Sample[0])
    # setup a queue of coordinates to fill
    Q = deque([(r,c) for r in range(nrow) for c in range(ncol) if \
    Sample[r][c] == '.'])
    S = sorted(list(Q))
    # fill in the coordinates
    while Q:
        xr,xc = Q.popleft()
        sr = set([Sample[xr][c] for c in range(ncol) if \
        Sample[xr][c] not in '.*'])
        sc = set([Sample[r][xc] for r in range(nrow) if \
        Sample[r][xc] not in '.*'])
        rune = sr & sc
        assert len(rune) <= 1
        if len(rune) == 1:
            rune = rune.pop()
            Sample[xr][xc] = rune
        else:
            Q.append( (xr,xc) )
    # construct the runic word
    word = ''.join([Sample[r][c] for r,c in S])
    return word

# parsing
X = [ l.strip().split(' ') for l in open(sys.argv[1], 'r') ]
Grid = []
ngcol = len(X[0])
ix0 = 0
for row in X:
    if len(row) == 1:
        ix0 += ngcol
        continue
    for ix1,col in enumerate(row):
        if len(Grid) <= ix0 + ix1:
            Grid.append([])
        Grid[ix0+ix1].append(list(col))

ans = 0
for Sample in Grid:
    word = get_word(Sample)
    pwr = 0
    for i,char in enumerate(word):
        pwr += (i+1) * (ord(char) - A + 1)
    ans += pwr
print(ans)

