import sys
import heapq

D = [(0,1), (1,0), (0,-1), (-1,0)]

def search_path(S, Cen, R, Vol, t_max, entry):
    nrow = len(Vol)
    ncol = len(Vol[0])
    assert S != Cen
    assert entry == (0,1) or entry == (0,-1)
    # determine the possible destinations
    if S[1] == Cen[1] and S[0] < Cen[0]:
        rng_r = range(Cen[0]+R+1,nrow)
    elif S[1] == Cen[1] and S[0] > Cen[1]:
        rng_r = range(0, Cen[0]-R)
    else:
        rng_r = range(Cen[0]+R+1,nrow)
    Path = {(r,Cen[1]): None for r in rng_r}
    # find the minimum path to each destination
    Q = []
    heapq.heappush(Q, (0, tuple(S), tuple(0 for (dr,dc) in D)) )
    Seen = {tuple(S): 0}
    while Q:
        step, (r,c), cnt = heapq.heappop(Q)
        # reject coordinates within the range of destruction
        if (Cen[1] - c) ** 2 + (Cen[0] - r) ** 2 <= R ** 2:
            continue
        # check if the path is too long
        if not any(min_step is None for min_step in Path.values()) and \
        step >= max(Path.values()):
            continue
        # continue the path to a new coordinate
        for di,(dr,dc) in enumerate(D):
            nr = r+dr
            nc = c+dc
            # check if the new coordinate is valid
            if not 0<=nr<nrow or not 0<=nc<ncol:
                continue
            # check if the new coordinate close enough
            step_next = step + Vol[nr][nc]
            if step_next >= t_max:
                continue
            # check if the new coordinate is unseen or a destination coordinate
            if (nr,nc) not in Path:
                if (nr,nc) in Seen and Seen[(nr,nc)] <= step_next:
                    continue
                Seen[(nr,nc)] = step_next
                cnt_next = tuple(cnt)
            else:
                cnt_next = list(cnt)
                cnt_next[di] += 1
                if cnt_next[ D.index(entry) ] > \
                cnt_next[ D.index( (-entry[0],-entry[1]) ) ]:
                    is_entry = True
                    if Path[(nr,nc)] is None or Path[(nr,nc)] > step_next:
                        Path[(nr,nc)] = step_next
                else:
                    is_entry = False
                if (nr,nc,is_entry) in Seen and \
                Seen[(nr,nc,is_entry)] <= step_next:
                    continue
                Seen[(nr,nc,is_entry)] = step_next
            # continue the search
            heapq.heappush(Q, (step_next, (nr,nc), cnt_next))
    return Path

# parsing
X = [list(l.strip()) for l in open(sys.argv[1], 'r')]
nrow = len(X)
ncol = len(X[0])
assert nrow == ncol
assert all(len(row) == ncol for row in X)
Vol = list(X)
Cen = []
S = []
for r in range(nrow):
    for c in range(ncol):
        if Vol[r][c] == '@':
            Vol[r][c] = 0
            Cen.append( (r,c) )
        elif Vol[r][c] == 'S':
            Vol[r][c] = 0
            S.append( (r,c) )
        else:
            Vol[r][c] = int(Vol[r][c])
assert len(Cen) == 1
assert len(S) == 1
Cen = Cen.pop()
S = S.pop()

# constraints
t_add = 30
R_add = 1

# find the shortest path to surround all the coordinates
Path = {}
min_path = None
for R in range(1, ncol // 2):
    t_max = (R*R_add + 1)*t_add
    Path_R = search_path(S, Cen, R, Vol, t_max, (0,-1))
    Path_L = search_path(S, Cen, R, Vol, t_max, (0,1))
    for (jr,jc) in Path_R:
        if Path_R[(jr,jc)] is None or Path_L[(jr,jc)] is None:
            continue
        step_tot = Path_R[(jr,jc)] + Path_L[(jr,jc)] - Vol[jr][jc]
        if step_tot < t_max and (min_path is None or min_path > step_tot):
            min_path = step_tot
    if min_path is not None:
        break

# calculate the final answer
ans = min_path * R
print(ans)

