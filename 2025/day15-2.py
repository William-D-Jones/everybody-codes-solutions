import sys
from collections import deque

D = [(-1,0), (0,1), (1,0), (0,-1)]

# parsing
X = open(sys.argv[1], 'r').read().strip().split(',')
Inst = [(x[0],int(x[1:])) for x in X]

W = set()
r,c = (0,0)
di = 0
for dx,n in Inst:
    if dx == 'L':
        di = (di-1) % len(D)
    elif dx == 'R':
        di = (di+1) % len(D)
    else:
        assert False
    dr,dc = D[di]
    for _ in range(n):
        r += dr
        c += dc
        W.add( (r,c) )
E = (r,c)
r_min = min(r for (r,c) in W)-1
r_max = max(r for (r,c) in W)+1
c_min = min(c for (r,c) in W)-1
c_max = max(c for (r,c) in W)+1
Seen = set([ (0,0) ])
min_step = None
Q = deque([ ((0,0), 0) ])
while Q:
    (r,c), step = Q.popleft()
    for dr,dc in D:
        nr = r+dr
        nc = c+dc
        if not (r_min<=nr<=r_max and c_min<=nc<=c_max) or \
        (nr,nc) in Seen or ((nr,nc) in W and (nr,nc) != E):
            continue
        Seen.add( (nr,nc) )
        if (nr,nc) == E:
            if min_step is None or step+1 < min_step:
                min_step = step+1
            continue
        Q.append( ((nr,nc), step+1) )
ans = min_step
print(ans)

