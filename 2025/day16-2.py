import sys
import math

# parsing
X = list(map(int,open(sys.argv[1], 'r').read().strip().split(',')))

ncol = len(X)
S = []
for f in range(1, ncol):
    if all( X[i-1] > 0 for i in range(f, ncol+1, f) ):
        S.append(f)
        X = [X[i]-(1 if (i+1) % f == 0 else 0) for i in range(len(X))]
        assert len(X) == ncol
ans = math.prod(S)
print(ans)

