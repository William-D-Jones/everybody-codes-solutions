import sys

NOV = {'a': 'A','b': 'B','c': 'C'}

# parsing
X = list(open(sys.argv[1], 'r').read().strip())

# constraints
nrep = 1000
dist = 1000

# I made the following simplifying observations about the problem:
# (i) The sequence is long enough that, for each repeat except the ends,
# all novices within the sequence can search a full 'dist' units in either
# direction without reaching the end of the sequence.
assert dist <= len(X)

ans = 0
for i,char in enumerate(X):
    if char not in NOV:
        continue
    kn = NOV[char]
    # setup the number of knights within, up-, or downstream of the repeat
    num_in = 0
    num_up = 0
    num_down = 0
    # pointers upstream and downstream of the repeat
    pnt_up = i
    pnt_down = i
    # count the knights
    for _ in range(dist):
        pnt_up -= 1
        pnt_down += 1
        if pnt_up >= 0 and X[pnt_up] == kn:
            num_in += 1
        if pnt_down < len(X) and X[pnt_down] == kn:
            num_in += 1
        if pnt_up < 0 and X[pnt_up % len(X)] == kn:
            num_up += 1
        if pnt_down >= len(X) and X[pnt_down % len(X)] == kn:
            num_down += 1
    ans += num_in * nrep + (nrep-1) * num_down + (nrep-1) * num_up
print(ans)

