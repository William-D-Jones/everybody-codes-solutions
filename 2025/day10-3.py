import sys
import functools

D = [(0,1), (1,0), (0,-1), (-1,0)]

# parsing
X = [list(l.strip()) for l in open(sys.argv[1], 'r')]
nrow = len(X)
ncol = len(X[0])
assert all(len(row) == ncol for row in X)
# find the dragon
Dragon = [(r,c) for r in range(nrow) for c in range(ncol) if X[r][c] == 'D']
assert len(Dragon) == 1
Dragon = Dragon.pop()
# find the sheep
Sheep = [(r,c) for r in range(nrow) for c in range(ncol) if X[r][c] == 'S']
assert len(set(sheep[1] for sheep in Sheep)) == len(Sheep)
# find the safe squares
Safe = set((r,c) for r in range(nrow) for c in range(ncol) if X[r][c] == '#')

@functools.cache
def get_dragon(qr, qc):
    """
    Returns the possible destination squares of the dragon.
    """
    Poss = []
    for dxi,(dr0,dc0) in enumerate(D):
        for perp in (1,3):
            dr1,dc1 = D[(dxi+perp) % len(D)]
            # get the new position of the dragon
            nr = qr + dr0 * 2 + dr1
            nc = qc + dc0 * 2 + dc1
            # check that the new position is valid
            if 0 <= nr < nrow and 0 <= nc < ncol:
                Poss.append( (nr,nc) )
    return Poss

@functools.cache
def get_games(qr, qc, S, turn):
    """
    Returns the number of winning games for the dragon from a given position.
    """
    # check if the game has been won
    if len(S) == 0:
        return 1
    if turn == 'S':
        # identify the sheep that can be moved
        S_Mv = [\
        (sr,sc) for (sr,sc) in S if sc != qc or sr+1 != qr or (sr+1,sc) in Safe\
        ]
        # check if a sheep move is possible
        if len(S_Mv) == 0:
            return get_games(qr, qc, S, 'D')
        if all(s_mv[0] == nrow-1 for s_mv in S_Mv):
            return 0
        # move a sheep
        return sum(get_games(\
        qr, qc, \
        tuple(sorted([(s_mv[0]+1,s_mv[1])] + [s for s in S if s != s_mv])), \
        'D' \
        ) for s_mv in S_Mv if s_mv[0] < nrow - 1 )
    elif turn == 'D':
        # get the possible moves of the dragon
        Poss = get_dragon(qr, qc)
        assert len(Poss) > 0
        # move the dragon and consume any sheep
        return sum(get_games(\
        nr, nc, tuple(s for s in S if s != (nr,nc) or s in Safe), 'S'\
        ) for (nr,nc) in Poss )
    else:
        assert False

ans = get_games(*Dragon, tuple(Sheep), 'S')
print(ans)

