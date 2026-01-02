import sys
import itertools

# parsing
X0, X1 = open(sys.argv[1], 'r').read().strip().split('\n\n')
Grid = [list(x.strip()) for x in X0.split('\n')]
Inst = [list(x.strip()) for x in X1.split('\n')]
nrow = len(Grid)
ncol = len(Grid[0])
assert all(len(row)==ncol for row in Grid)

# try every token in every slot
Coin = {}
for ix_token, inst in enumerate(Inst):
    for ix in range( (ncol+1)//2 ):
        pnt = 0
        r = -1
        c = 2*ix
        while r+1<nrow:
            if Grid[r+1][c] == '.':
                pass
            elif Grid[r+1][c] == '*':
                if inst[pnt] == 'L':
                    dc = -1
                elif inst[pnt] == 'R':
                    dc = 1
                else:
                    assert False
                if 0<=c+dc<ncol:
                    c += dc
                else:
                    c -= dc
                pnt += 1
            else:
                assert False
            r += 1
        assert c % 2 == 0
        slot_in = ix+1
        slot_out = c // 2 + 1
        coin = max(0, slot_out * 2 - slot_in)
        Coin[ (ix_token, slot_in) ] = coin

# determine the minimum and maximum arrangements of tokens in initial slots
min_coin = ( ( (ncol+1)//2 ) * 2 - 1 ) * len(Inst)
max_coin = 0
ix = 0
for SS in itertools.combinations(range((ncol+1)//2), len(Inst)):
    for TT in itertools.permutations([i for i in range(len(Inst))]):
        coin = sum([ Coin[(tt, ss+1)] for tt,ss in zip(TT,SS)])
        min_coin = min(min_coin, coin)
        max_coin = max(max_coin, coin)
        ix += 1
ans = ' '.join([str(min_coin), str(max_coin)])
print(ans)

