import sys
from collections import deque, Counter

D = [(0,1), (1,0), (0,-1), (-1,0)]

# parsing
X = [list(l.strip()) for l in open(sys.argv[1], 'r')]
nrow = len(X)
ncol = len(X[0])
assert all( len(row)==ncol for row in X )

# find the starting position
S = [(r,c) for r in range(nrow) for c in range(ncol) if X[r][c]=='S']
assert len(S)==1
S = S.pop()

# constraints
a_start = 384400

# The goal is to travel the furthest possible downward. Therefore, we want to
# pick a path that contains the most + symbols, the least - symbols, and the
# least # symbols, which require a detour. Lateral movements should be avoided
# whenever possible. With these goals in mind, we can make some simplifying 
# observations regarding the input:
# (i) There exist columns containing + squares but no # or - squares:
Cnt_Plus = []
Loss = {}
Trough = {}
for c in range(ncol):
    Col = [X[r][c] for r in range(nrow)]
    Cnt = Counter(Col)
    if Cnt['+'] > 0 and Cnt['-']==0 and Cnt['#']==0:
        Cnt_Plus.append( (Cnt['+'], c) )
    run = 0
    trough = 0
    for r in range(nrow):
        if X[r][c] in '.S':
            run -= 1
        elif X[r][c] == '-':
            run -= 2
        elif X[r][c] == '+':
            run += 1
        else:
            assert X[r][c] == '#'
        trough = min(trough, run)
    Trough[c] = trough
    Loss[c] = Cnt['-'] * -2 + Cnt['.'] * -1 + Cnt['S'] * -1 + Cnt['+']
    assert Loss[c] < 0 or all(X[r][c]=='#' for r in range(nrow))
assert len(Cnt_Plus)>0
# (ii) Upon reaching a column containing the maximum possible number of +
# squares, we should simply fly straight downward, maximizing the distance
# traveled downward:
max_plus = max(cnt for cnt,c in Cnt_Plus)
Col_Plus = set(c for cnt,c in Cnt_Plus if cnt==max_plus)

Q = deque([(a_start, tuple(S))])
Seen = { ((0,0)): a_start }
last = 0
dist_max = 0
while Q:
    a, (r,c) = Q.popleft()
    # check if the journey is complete
    if a <= 0:
        dist_max = max(dist_max, r)
        continue
    if r >= nrow and c not in Col_Plus:
        continue
    for dr,dc in D:
        # get the new coordinate
        nr = r+dr
        nc = c+dc
        # check that the new coordinate is valid
        if not 0<=nr or not 0<=nc<ncol or X[nr%nrow][nc] in '#':
            continue
        # get the new altitude
        if X[nr%nrow][nc] in '.S':
            da = -1
        elif X[nr%nrow][nc] == '-':
            da = -2
        elif X[nr%nrow][nc] == '+':
            da = 1
        else:
            assert False
        a_next = a+da
        # check if the state has been seen
        State = ((nr,nc))
        if State in Seen and Seen[State]>=a_next:
            continue
        Seen[State] = a_next
        # if we have reached a plus column, travel downward as far as possible
        if nc in Col_Plus and nr%nrow == nrow-1 and a_next>0:
            n_rep = max(0, a_next - abs(Trough[nc])) // abs(Loss[nc])
            nr += n_rep * nrow
            a_next += n_rep * Loss[nc]
        # continue the journey
        Q.append( (a_next, (nr,nc)) )
ans = dist_max
print(ans)

