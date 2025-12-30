import sys

# parsing
X1,X2 = open(sys.argv[1], 'r').read().strip().split('\n\n')
Key = list(X1)
Grid = [list(l) for l in X2.split('\n')]
nrow = len(Grid)
ncol = len(Grid[0])
assert all( len(row)==ncol for row in Grid )

# constraints
n = 1048576000

# simulate one round of decoding for each coordinate
Round = {(r,c): (r,c) for r in range(nrow) for c in range(ncol)}
pnt = 0
for gr in range(1,nrow-1):
    for gc in range(1,ncol-1):
        # extract the elements to rotate, clockwise from top left
        r,c = gr-1,gc-1
        Pos = [(gr-1,gc-1), (gr-1,gc), (gr-1,gc+1), (gr,gc+1), (gr+1,gc+1), \
        (gr+1,gc), (gr+1,gc-1), (gr,gc-1)]
        Char = [Round[pos] for pos in Pos]
        # rotate the characters
        if Key[pnt] == 'L':
            Char_Next = Char[1:] + Char[0:1]
        elif Key[pnt] == 'R':
            Char_Next = Char[-1:] + Char[0:-1]
        else:
            assert False
        # replace the characters
        for i in range(len(Pos)):
            Round[ Pos[i] ] = Char_Next[i]
        # augment the key pointer
        pnt = (pnt+1) % len(Key)
Pos_Nxt = {(r,c): (nr,nc) for (nr,nc),(r,c) in Round.items()}

# simulate decoding until a repeated position is found for each coordinate
Hist = {(r,c): [(r,c)] for r in range(nrow) for c in range(ncol)}
Q = {(r,c) for r in range(nrow) for c in range(ncol)}
while Q:
    gr,gc = Q.pop() # get a point of interest to track
    r,c = gr,gc
    while True:
        r,c = Pos_Nxt[(r,c)]
        Hist[(gr,gc)].append((r,c))
        if r==gr and c==gc:
            break
        else:
            continue

# analyze repeats to decode the grid
Grid_Out = [(['.'] * ncol) for _ in range(nrow)]
for gr in range(nrow):
    for gc in range(ncol):
        ix_rep = 0
        len_rep = len(Hist[(gr,gc)]) - ix_rep - 1
        if n > ix_rep:
            n_rep = (n-ix_rep) // len_rep
            ix = n - len_rep*n_rep
        else:
            ix = n
        r,c = Hist[(gr,gc)][ix]
        Grid_Out[r][c] = Grid[gr][gc]

# print the message
S = [(r,c) for r in range(nrow) for c in range(ncol) if Grid_Out[r][c]=='>']
E = [(r,c) for r in range(nrow) for c in range(ncol) if Grid_Out[r][c]=='<']
assert len(S)==1 and len(E)==1
S = S.pop()
E = E.pop()
assert E[0]==S[0]
Out = ''.join(Grid_Out[S[0]][S[1]+1:E[1]])
print(Out)

