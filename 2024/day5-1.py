import sys

# parsing
X = [ list(map(int, l.strip().split())) for l in open(sys.argv[1], 'r') ]
nrow = len(X)
ncol = len(X[0])
# collect columns
C = [ [X[r][c] for r in range(nrow)] for c in range(ncol) ]

c0 = 0
S = []
for _ in range(10):
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
    S.append(int(''.join([str(C[c][0]) for c in range(ncol)])))
    # identify the column of the next clapper
    c0 = (c0 + 1) % ncol
ans = S[-1]
print(ans)
    
