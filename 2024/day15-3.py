import sys
import heapq

D = [(0,1), (1,0), (0,-1), (-1,0)]
A = ord('A')
Z = ord('Z')

def find_herbs(S, E, Col, Block = []):
    min_step = None
    Seen = {(S, ''): 0}
    Q = []
    heapq.heappush(Q, (len(Col), 0, S, set()))
    ix = 0
    while Q:
        ix += 1
        todo, step, (r,c), Herb = heapq.heappop(Q)
        # check if we have taken too many steps
        if min_step is not None and step + 1 >= min_step:
            continue
        for dr,dc in D:
            # compute the new coordinate and check if it is valid
            nr = r+dr
            nc = c+dc
            if not 0<=nr<nrow or not 0<=nc<ncol or X[nr][nc] in '#~' or \
            (nr,nc) in Block:
                continue
            # pick up an herb if one is available
            Herb_Next = set(Herb)
            if A<=ord(X[nr][nc])<=Z:
                Herb_Next.add(X[nr][nc])
            # skip states that have been seen before
            step_next = step + 1
            State = ( (nr,nc), ''.join(sorted(list(Herb_Next))) )
            if State in Seen and Seen[State] <= step_next:
                continue
            Seen[State] = step_next
            # check if we have finished the journey
            if (nr,nc) == E and Col <= Herb_Next:
                if min_step is None or min_step > step_next:
                    min_step = step_next
            else:
                heapq.heappush( Q, \
                (len(Col)-len(Herb_Next), step_next, (nr,nc), Herb_Next) )
    return min_step

# parsing
X = [list(l.strip()) for l in open(sys.argv[1], 'r')]
nrow = len(X)
ncol = len(X[0])
assert all(len(row) == ncol for row in X)

# find the starting position
S = [(0,c) for c in range(ncol) if X[0][c] == '.']
assert len(S) == 1
S = S.pop()

# items to be collected
Col = set(X[r][c] for r in range(nrow) for c in range(ncol) if \
A<=ord(X[r][c])<=Z)

# To solve the problem, we need to force all paths to travel through 2 distinct
# passageways at the bottom of the grid, collecting all items in each section of
# the grid:
ans2 = \
find_herbs(S, S, set(['G','H','I','J','K','R','E']), [(73,83),(73,171)]) + \
find_herbs((75,83), (75,83), set(['A','B','C','D']), [(75,85)]) + \
find_herbs((75,171), (75,171), set(['N','O','P','Q']), [(75,169)])
print(ans2)

