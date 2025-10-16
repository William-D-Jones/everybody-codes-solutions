import sys

# parsing
X = [ int(l.strip()) for l in open(sys.argv[1], 'r') ]

ans = sum(abs(x - sorted(X)[len(X)//2]) for x in X)
print(ans)

