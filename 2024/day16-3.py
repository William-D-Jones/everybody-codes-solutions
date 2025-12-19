import sys
from collections import Counter
import heapq

# parsing
X0, X1 = open(sys.argv[1], 'r').read().strip().split('\n\n')
Turn = list(map(int, X0.split(',')))
Wheel = [[] for turn in Turn]
nchar = 3
for x in X1.split('\n'):
    Face = [ x[ (nchar+1)*i : (nchar+1)*i+nchar ] for \
    i in range( (len(x)+1) // (nchar+1) )]
    for i,face in enumerate(Face):
        if face != ' '*nchar:
            face = face[0:1] + face[2:3] # drop the muzzle
            Wheel[i].append(face)

# constraints
n = 256
min_coin = 3

# get the minimum wins
Q = []
heapq.heappush( Q, (0, 0, tuple(0 for _ in Turn)) )
Seen = {tuple(0 for _ in Turn): (0,0)}
min_win = None
while Q:
    win, pull, pnt = heapq.heappop(Q)
    # check if we have finished the pulls
    if pull >= n:
        if min_win is None or win<min_win:
            min_win = win
        continue
    # check if we have exceeded the minimum
    if min_win is not None and win>=min_win:
        continue
    # simulate pulls
    for adj in (-1, 0, 1):
        # perform the pull
        pnt_next = list(pnt)
        Face = []
        for i,turn in enumerate(Turn):
            pnt_next[i] = (pnt_next[i] + turn + adj) % len(Wheel[i])
            Face.append( Wheel[i][ pnt_next[i] ] )
        C = Counter(list(''.join(Face)))
        win_next = win + \
        sum(num-min_coin+1 for num in C.values() if num >= min_coin)
        # prune repeated states
        pnt_next = tuple(pnt_next)
        pull_next = pull+1
        if pnt_next in Seen:
            seen_win, seen_pull = Seen[pnt_next]
            if seen_win<=win_next and seen_pull>=pull_next:
                continue
        Seen[pnt_next] = (win_next, pull_next)
        # continue the search
        heapq.heappush( Q, (win_next, pull_next, pnt_next) )

# get the maximum wins
Q = []
heapq.heappush( Q, (0, 0, tuple(0 for _ in Turn)) )
Seen = {tuple(0 for _ in Turn): (0,0)}
max_win = None # recorded as a negative number for use with heapq
while Q:
    win, pull, pnt = heapq.heappop(Q)
    # check if we have finished the pulls
    if pull >= n:
        if max_win is None or win<max_win:
            max_win = win
        continue
    # simulate pulls
    for adj in (-1, 0, 1):
        # perform the pull
        pnt_next = list(pnt)
        Face = []
        for i,turn in enumerate(Turn):
            pnt_next[i] = (pnt_next[i] + turn + adj) % len(Wheel[i])
            Face.append( Wheel[i][ pnt_next[i] ] )
        C = Counter(list(''.join(Face)))
        win_next = win - \
        sum(num-min_coin+1 for num in C.values() if num >= min_coin)
        # prune repeated states
        pnt_next = tuple(pnt_next)
        pull_next = pull+1
        if pnt_next in Seen:
            seen_win, seen_pull = Seen[pnt_next]
            if seen_win<=win_next and seen_pull<=pull_next:
                continue
        Seen[pnt_next] = (win_next, pull_next)
        # continue the search
        heapq.heappush( Q, (win_next, pull_next, pnt_next) )

# produce the final answer
ans = str(-1*max_win) + ' ' + str(min_win)
print(ans)

