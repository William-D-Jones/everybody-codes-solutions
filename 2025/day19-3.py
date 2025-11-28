import sys
from collections import deque
import math

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
    # identify the next column with a passageway
    nc = min(pc for (pc,pr,psz) in X if pc > c)
    # collect all the passageways on the new column
    P = [(pc,pr,psz) for (pc,pr,psz) in X if pc == nc]
    for pc,pr,psz in P:
        # Let f be the number of flaps.
        # Then:
        # nr = r + f - (nc-c-f) = r+f-nc+c+f = 2*f + r-nc+c
        # We must have that pr<=nr<pr+psz, so pr<=nr<=pr+psz-1.
        # Hence:
        # pr <= 2*f + r-nc+c
        # pr - (r-nc+c) <= 2*f
        # f >= (pr-(r-nc+c) / 2)
        # And:
        # 2*f + r-nc+c <= pr+psz-1
        # 2*f <= pr+psz-1 - (r-nc+c)
        # f <= (pr+psz-1 - (r-nc+c)) / 2
        # determine the minimum flaps to clear the passageway
        flap = max(0, \
        min( math.ceil( ( pr-(r-nc+c) ) / 2 ), (pr+psz-1-(r-nc+c)) // 2 ) \
        )
        nr = 2 * flap + (r - nc + c)
        if not pr<=nr<pr+psz:
            continue
        # augment the flap counter
        step_next = step + flap
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
                
