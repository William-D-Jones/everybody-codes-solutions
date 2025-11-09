import sys
from collections import deque

D = [(0,1), (1,0), (0,-1), (-1,0)]

# parsing
X = [list(l.strip()) for l in open(sys.argv[1], 'r')]
nrow = len(X)
ncol = len(X[0]) 
assert all(len(row) == ncol for row in X)
# find the starting positions
S = [(r,c) for r in range(nrow) for c in range(ncol) if X[r][c] == 'S']

# constraints
h_min = 0
h_max = 9

# walk the maze
Q = deque([[(r,c), set([(r,c)]), 0] for (r,c) in S])
Time = {(r,c): 0 for (r,c) in S}
t_min = None
while Q:
    (r,c), Seen, t = Q.popleft()
    for dr,dc in D:
        nr,nc = r+dr,c+dc
        # check if the new coordinate is valid and unseen
        if not 0 <= nr < nrow or not 0 <= nc < ncol or (nr,nc) in Seen or \
        X[nr][nc] in '# ':
            continue
        # get the height difference
        el = int(X[r][c]) if X[r][c] not in 'SE' else 0
        el_next = int(X[nr][nc]) if X[nr][nc] not in 'SE' else 0
        if el_next > el:
            el_up = el_next - el
            el_down = el + 1 + h_max - el_next
            el_step = min(el_up, el_down)
        elif el_next < el:
            el_up = h_max - el + 1 + el_next
            el_down = el - el_next
            el_step = min(el_up, el_down)
        else:
            el_step = 0
        t_next = t + 1 + el_step
        if (nr,nc) not in Time:
            Time[(nr,nc)] = t_next
        else:
            if Time[(nr,nc)] <= t_next:
                continue
            else:
                Time[(nr,nc)] = t_next
        # check if we have reached the end
        if X[nr][nc] == 'E':
            if t_min is None or t_min > t_next:
                t_min = t_next
        else:
            Q.append( [(nr,nc), Seen | set([(nr,nc)]), t_next] )
ans = t_min
print(ans)

