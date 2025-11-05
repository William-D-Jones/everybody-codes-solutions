import sys
from collections import Counter

# parsing
X = [int(x) for x in open(sys.argv[1], 'r').read().strip().split(',')]

C = Counter(X)
ans = max(C.values())
print(ans)

