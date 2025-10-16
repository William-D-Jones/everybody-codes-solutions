import sys
from collections import deque, Counter

# parsing
X = [ list(l.strip().split(':')) for l in open(sys.argv[1], 'r') ]
T = {}
for par,chi in X:
    T[par] = list(chi.split(','))

# trace the branches
Q = deque([('RR',)])
F = []
while Q:
    P = Q.popleft()
    if P[-1] not in T.keys():
        continue
    for chi in T[P[-1]]:
        if chi == '@':
            F.append( tuple(list(P) + [chi]) )
        if chi == 'BUG' or chi == 'ANT':
            continue
        else:
            Q.append( tuple(list(P) + [chi]) )

# identify the path to the powerful fruit
F_Len = Counter([len(P) for P in F])
len_power = set( len_path for len_path,cnt in F_Len.items() if cnt == 1 )
assert len(len_power) == 1
len_power = len_power.pop()
path_power = set( P for P in F if len(P) == len_power )
assert len(path_power) == 1
path_power = path_power.pop()
ans = ''.join(node[0] for node in path_power)
print(ans)

