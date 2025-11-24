import sys

# parsing
X = list(map(int,open(sys.argv[1], 'r').read().strip().split(',')))

# constraints
ncol = 90

ans = sum(ncol // x for x in X)
print(ans)
    
