import sys
from collections import deque

# parsing
X = [ int(l.strip()) for l in open(sys.argv[1], 'r') ]

# constraints
T = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
max_diff = 100

# identify the maximum sum we need to identify
max_tot = max(X)

# construct random sums until we reach the maximum
A = set(T)
Tot = {}
Q = deque([tuple()])
while Q:
    s = Q.popleft()
    for a in A:
        ns = s + (a,)
        tot = sum(ns)
        if tot not in Tot.keys():
            if tot <= max_tot:
                Tot[tot] = ns
            if tot < max_tot:
                Q.append(ns)
        else:
            continue

# extract the minimum number of terms for each total
ans = 0
for tot in X:
    if any(a <= max_diff for a in Tot[tot]):
        ans += len(Tot[tot])
    else:
        min_term = None
        for diff in range(max_diff+1):
            if (tot - diff) % 2 != 0:
                continue
            t1 = (tot - diff) // 2
            t2 = t1 + diff
            n_term = len(Tot[t1]) + len(Tot[t2])
            if min_term is None or n_term < min_term:
                min_term = n_term
        ans += min_term
print(ans)
    
