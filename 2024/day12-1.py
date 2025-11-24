import sys

# parsing
X = [list(l.strip()) for l in open(sys.argv[1], 'r')]
# get the dimensions of the diagram
nrow = len(X)
ncol = len(X[0])
assert all(len(row) == ncol for row in X)
assert X[-1] == ['='] * ncol
# setup a coordinate system, defining the top right of the diagram as (0,0)
# find the targets and sources
Tar = []
Src = {}
for r in range(nrow):
    for c in range(ncol):
        if X[r][c] == 'T':
            Tar.append( (r,c) )
        elif X[r][c] in 'ABC':
            Src[ (r,c) ] = X[r][c]
        elif X[r][c] in '.=':
            pass
        else:
            assert False
# get the column of the catapult
ccat = set(src[1] for src in Src)
assert len(ccat) == 1
ccat = ccat.pop()

# determine the shots to be taken, which should be taken in the order parsed
ans = 0
for r,c in Tar:
    # get the column-wise distance between the catapoult and the target
    dc = c - ccat
    assert dc > 0
    # determine the power needed to hit the target
    pwr = (dc + nrow - 2 - r) // 3
    height = dc + nrow - 2 - r - pwr * 3
    # determine the launching position from the catapoult
    src = Src[ (nrow - 2 - height, ccat) ]
    ans += pwr * (ord(src) - ord('A') + 1)
print(ans)

