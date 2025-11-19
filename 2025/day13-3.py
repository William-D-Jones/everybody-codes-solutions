import sys

# parsing
X = [tuple(map(int,l.strip().split('-'))) for l in open(sys.argv[1], 'r')]
assert all(len(x) == 2 for x in X)

# constraints
n_trn = 202520252025

# construct the dial
Dial = [(1,1)] + \
[X[i] for i in range(len(X)) if i % 2 == 0] + \
[X[i][::-1] for i in range(len(X)) if i % 2 != 0][::-1]

# turn the dial
len_dial = 1 + sum(x[1]-x[0]+1 for x in X)
ix_turn = (0 + n_trn) % len_dial
pnt = 0
ix_range = 0
while pnt <= ix_turn:
    start, end = Dial[ix_range]
    len_range = abs(start - end) + 1
    if pnt + len_range - 1 < ix_turn:
        pnt += len_range
        ix_range += 1
    else:
        if end >= start:
            ans = start + ix_turn - pnt
            break
        elif end < start:
            ans = start - (ix_turn - pnt)
            break
print(ans)

