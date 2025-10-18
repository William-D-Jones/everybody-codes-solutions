import sys
from collections import Counter

# parsing
X = [ list(map(int, l.strip().split())) for l in open(sys.argv[1], 'r') ]
nrow = len(X)
ncol = len(X[0])
# collect columns
C = [ [X[r][c] for r in range(nrow)] for c in range(ncol) ]

Seen = Counter()
c0 = 0
num_rep = 2024
max_rep = 0
ix = 0
while max_rep < num_rep:
    ix += 1
    # get the clapper and remove them from the source column
    n0 = C[c0].pop(0)
    # identify the target column
    c1 = (c0 + 1) % ncol
    # insert the clapper into the target column
    p1 = n0 % (2 * len(C[c1]))
    if n0 <= len(C[c1]):
        C[c1] = C[c1][:p1-1] + [n0] + C[c1][p1-1:]
    else:
        C[c1] = C[c1][:2*len(C[c1])-p1+1] + [n0] + C[c1][2*len(C[c1])-p1+1:]
    # get the column leaders
    s = int(''.join([str(C[c][0]) for c in range(ncol)]))
    Seen[s] += 1
    if Seen[s] > max_rep:
        max_rep = Seen[s]
    # identify the column of the next clapper
    c0 = (c0 + 1) % ncol
ans = ix * sorted([(n,s) for s,n in Seen.items()])[-1][1]
print(ans)

