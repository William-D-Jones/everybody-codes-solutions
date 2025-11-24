import sys

# parsing
X = list(map(int,open(sys.argv[1], 'r').read().strip().split(',')))

# constraints
n_block = 202520252025000

# determine the spell needed
ncol = len(X)
S = []
for f in range(1, ncol):
    if all( X[i-1] > 0 for i in range(f, ncol+1, f) ):
        S.append(f)
        X = [X[i]-(1 if (i+1) % f == 0 else 0) for i in range(len(X))]
        assert len(X) == ncol

# calculate the number of columns
ntot = 0
delta = 1
while not( sum(ntot // f for f in S) <= n_block and \
sum((ntot+delta) // f for f in S) > n_block and delta == 1 ):
    if sum((ntot+delta) // f for f in S) <= n_block:
        ntot += delta
        delta *= 10
    else:
        delta = max(1, delta // 10)
ans = ntot
print(ans)

