import sys

# parsing
X0, X1 = open(sys.argv[1], 'r').read().strip().split('\n\n')
Grid = [list(x.strip()) for x in X0.split('\n')]
Inst = [list(x.strip()) for x in X1.split('\n')]
nrow = len(Grid)
ncol = len(Grid[0])
assert all(len(row)==ncol for row in Grid)
assert (ncol+1) // 2 == len(Inst)

ans = 0
for ix,inst in enumerate(Inst):
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
    ans += coin
print(ans)

