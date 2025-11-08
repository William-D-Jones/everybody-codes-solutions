import sys
import math

# parsing
X = [tuple(map(int,l.strip().split('|'))) for l in open(sys.argv[1], 'r')]

# constraints
n1 = 100

ans = X[0][0] * n1 * math.prod(X[i][1] for i in range(2,len(X)-1)) // \
( math.prod(X[i][0] for i in range(2,len(X)-1)) * X[-1][0] )
print(ans)

