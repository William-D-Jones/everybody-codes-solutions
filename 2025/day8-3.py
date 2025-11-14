import sys
from collections import Counter
import itertools

# parsing
X = list(map(int,open(sys.argv[1], 'r').read().strip().split(',')))

# constraints
n_nail = 256

# construct the crossings
Cross = Counter()
for i in range(len(X)-1):
    start = X[i]-1
    end = X[i+1]-1
    Cross[ tuple(sorted([start,end])) ] += 1

# find the maximum number of crossings that can be cut
ans = 0
for start,end in itertools.combinations(list(range(n_nail)), 2):
    # find the numbers to the left and right of the starting position
    if end > start:
        Left = list(range(start+1, end))
        Right = list(range(end+1, n_nail)) + list(range(0, start))
    elif end < start:
        Left = list(range(start+1, n_nail)) + list(range(0, end))
        Right = list(range(end+1, start))
    else:
        assert False
    # count the number of counts
    num_cut = Cross[ tuple(sorted([start,end])) ]
    for l in Left:
        for r in Right:
            num_cut += Cross[ tuple(sorted([l,r])) ]
    ans = max(ans, num_cut)
print(ans)

