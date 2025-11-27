import sys
from collections import deque

D = [(-1,0), (0,1), (1,0), (0,-1)]
DD = [(-1,1), (1,1), (1,-1), (-1,-1)]

def is_reachable(Start, End, Walls):
    if Start[0]!=End[0] and Start[1]!=End[1]:
        return False
    vr_min = min(Start[0],End[0])
    vr_max = max(Start[0],End[0])
    vc_min = min(Start[1],End[1])
    vc_max = max(Start[1],End[1])
    for (r0,c0),(r1,c1) in Walls:
        wr_min = min(r0,r1)
        wr_max = max(r0,r1)
        wc_min = min(c0,c1)
        wc_max = max(c0,c1)
        if min(vr_max,wr_max)-max(vr_min,wr_min) >= 0 and \
        min(vc_max,wc_max)-max(vc_min,wc_min) >= 0:
            return False
    return True

# parsing
X = open(sys.argv[1], 'r').read().strip().split(',')
Inst = [(x[0],int(x[1:])) for x in X]

# construct the walls and identify the wall vertices
W = []
V = set()
r,c = (0,0)
di = 0
for i,(dx,n) in enumerate(Inst):
    if dx == 'L':
        di = (di-1) % len(D)
    elif dx == 'R':
        di = (di+1) % len(D)
    else:
        assert False
    dr,dc = D[di]
    if i == 0:
        W.append( tuple(sorted([(r+dr,c+dc), (r+dr*n, c+dc*n)])) )
        V.add( (r+dr,c+dc) )
    elif i == len(Inst)-1:
        W.append( tuple(sorted([(r,c), (r+dr*(n-1), c+dc*(n-1))])) )
    else:
        W.append( tuple(sorted([(r,c), (r+dr*n, c+dc*n)])) )
    r += dr * n
    c += dc * n
    if i < len(Inst)-1:
        V.add( (r,c) )

# record the end coordinate
E = (r,c)

# identify all coordinates diagonally adjacent to the wall vertices
VV = set([E])
for (r,c) in V:
    for dr,dc in DD:
        VV.add( (r+dr,c+dc) )

# get the wall ranges
r_min = min(r for (r,c) in V)-1
r_max = max(r for (r,c) in V)+1
c_min = min(c for (r,c) in V)-1
c_max = max(c for (r,c) in V)+1

# find the shortest path
Seen = {(0,0): 0}
min_step = None
min_path = None
Q = deque([ ((0,0), 0) ])
while Q:
    (r,c), step = Q.popleft()
    if (min_step is not None and min_step <= step) or Seen[(r,c)] < step:
        continue
    for dr,dc in D:
        Dest = set()
        # find reachable vertices
        for (vr,vc) in VV:
            # check if the vertex can be reached directly
            if is_reachable( (r,c), (vr,vc), W ):
                if (abs(vr-r) > 0 and (vr-r) // abs(vr-r) == dr) or \
                (abs(vc-c) > 0 and (vc-c) // abs(vc-c) == dc):
                    Dest.add( (vr,vc) )
                else:
                    continue
            else:
                # get the layover coordinate on the way to the vertex
                if dr != 0 and abs(vr-r) > 0 and (vr-r) // abs(vr-r) == dr:
                    Layover = (vr,c)
                elif dc != 0 and abs(vc-c) > 0 and (vc-c) // abs(vc-c) == dc:
                    Layover = (r,vc)
                else:
                    continue
                # check if the layover and target coordinates are reachable
                if is_reachable( (r,c), Layover, W ) and \
                is_reachable( Layover, (vr,vc), W ):
                    Dest.add( (vr,vc) )
        # add new starting points to the queue
        for (nr,nc) in Dest:
            # adjust the step counter
            step_next = step+abs(nr-r)+abs(nc-c)
            # check if the end coordinate has been reached
            if (nr,nc) == E:
                if min_step is None or step_next < min_step:
                    min_step = step_next
                continue
            # continue the journey from the new starting coordinate
            if (nr,nc) not in Seen or Seen[(nr,nc)] > step_next:
                Q.append( ( (nr,nc), step_next ) )
                Seen[(nr,nc)] = step_next
ans = min_step
print(ans)

