import sys

# parsing
X1,X2 = open(sys.argv[1], 'r').read().strip().split('\n\n')
Key = list(X1)
Grid = [list(l) for l in X2.split('\n')]
nrow = len(Grid)
ncol = len(Grid[0])
assert all( len(row)==ncol for row in Grid )

# constraints
n = 100

# rotate the grid as instructed
for _ in range(n):
    pnt = 0
    for r in range(1,nrow-1):
        for c in range(1,ncol-1):
            # extract the characters to rotate
            Char = Grid[r-1][c-1:c+2] + Grid[r][c+1:c+2] + \
            Grid[r+1][c-1:c+2][::-1] + Grid[r][c-1:c]
            # rotate the characters
            if Key[pnt] == 'L':
                Char = Char[1:] + Char[0:1]
            elif Key[pnt] == 'R':
                Char = Char[-1:] + Char[0:-1]
            else:
                assert False
            # replace the characters
            Grid[r-1][c-1:c+2] = Char[0:3]
            Grid[r][c+1:c+2] = Char[3:4]
            Grid[r+1][c-1:c+2] = Char[4:7][::-1]
            Grid[r][c-1:c] = Char[7:]
            # augment the key pointer
            pnt = (pnt+1) % len(Key)

# print the message
S = [(r,c) for r in range(nrow) for c in range(ncol) if Grid[r][c]=='>']
E = [(r,c) for r in range(nrow) for c in range(ncol) if Grid[r][c]=='<']
assert len(S)==1 and len(E)==1
S = S.pop()
E = E.pop()
assert E[0]==S[0]
Out = ''.join(Grid[S[0]][S[1]+1:E[1]])
print(Out)

