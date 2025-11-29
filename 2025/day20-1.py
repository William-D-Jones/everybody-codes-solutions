import sys

# parsing
X = [list(l.strip()) for l in open(sys.argv[1], 'r')]
nrow = len(X)
ncol = len(X[0])
assert all(len(row) == ncol for row in X)

ans = 0
for r in range(nrow-1):
    for c in range(ncol-1):
        # count horizontally adjacent trampolines
        if X[r][c] == 'T' and X[r][c+1] == 'T':
            ans += 1
        # count vertically adjacent trampolines
        if X[r][c] == 'T' and X[r+1][c] == 'T' and \
        r % 2 != c % 2:
            ans += 1
print(ans)

