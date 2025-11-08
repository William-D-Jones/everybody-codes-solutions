import sys

# parsing
X = [int(l.strip()) for l in open(sys.argv[1], 'r')]

# constraints
n1 = 2025

ans = n1 * X[0] // X[-1]
print(ans)

