import sys

# parsing
X = [ int(l.strip()) for l in open(sys.argv[1], 'r') ]

ans = sum(x - min(X) for x in X)
print(ans)

