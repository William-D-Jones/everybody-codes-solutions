import sys
import math

# parsing
X = [int(l.strip()) for l in open(sys.argv[1], 'r')]

# constraints
nn = 10000000000000

ans = math.ceil(X[-1] * nn / X[0])
print(ans)

