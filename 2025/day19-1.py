import sys
from collections import deque

D = [(1,1), (-1,1)]

# parsing
X = [tuple(map(int,l.strip().split(','))) for l in open(sys.argv[1], 'r')]

# get the coordinate of the last passage
pc_max = max(pc for (pc,pr,psz) in X)

S = (0,0)
Q = deque([ (tuple(S), 0) ])
Seen = {(0,0): 0}
min_step = None
while Q:
    (r,c), step = Q.popleft()
    for dr,dc in D:
        nr = r+dr
        nc = c+dc
        # collect all the passageways on the current column
        P = [(pc,pr,psz) for (pc,pr,psz) in X if pc == nc]
        # check if we are inside one of the passageways
        free = True if not P else False
        for pc,pr,psz in P:
            if pr<=nr<pr+psz:
                free = True
        # check if the new coordinate is valid
        if not free:
            continue
        # augment the flap counter
        step_next = step + (1 if dr > 0 else 0)
        # check if we have visited the coordinate before
        if (nr,nc) in Seen and Seen[(nr,nc)] <= step_next:
            continue
        Seen[(nr,nc)] = step_next
        # check if we have completed the journey
        if nc == pc_max:
            if min_step is None or min_step > step_next:
                min_step = step_next
            continue
        # continue the journey
        Q.append( ((nr,nc), step_next) )
ans = min_step
print(ans)
                
