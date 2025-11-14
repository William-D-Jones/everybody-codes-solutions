import sys
from collections import Counter

# parsing
X = list(map(int,open(sys.argv[1], 'r').read().strip().split(',')))

# constraints
n_nail = 256

Cross = Counter()
ans = 0
for i in range(len(X)-1):
    start = X[i]-1
    end = X[i+1]-1
    # find the numbers to the left and right of the starting position
    if end > start:
        Left = list(range(start+1, end))
        Right = list(range(end+1, n_nail)) + list(range(0, start))
    elif end < start:
        Left = list(range(start+1, n_nail)) + list(range(0, end))
        Right = list(range(end+1, start))
    else:
        assert False
    # count the crossings
    for l in Left:
        for r in Right:
            ans += Cross[ tuple(sorted([l,r])) ]
    Cross[ tuple(sorted([start,end])) ] += 1
print(ans)

