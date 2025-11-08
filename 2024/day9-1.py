import sys
from collections import deque

# parsing
X = [ int(l.strip()) for l in open(sys.argv[1], 'r') ]

# constraints
T = [1, 3, 5, 10]

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
ans = sum(len(Tot[tot]) for tot in X)
print(ans)
    
