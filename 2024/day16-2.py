import sys
from collections import Counter

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
n = 202420242024
min_coin = 3

# simulate pulls until we find a repeat
ans = 0
Pnt = []
Win = []
pnt = [0 for _ in Turn]
for ix in range(n):
    Face = []
    for i,turn in enumerate(Turn):
        pnt[i] = (pnt[i] + turn) % len(Wheel[i])
        Face.append( Wheel[i][ pnt[i] ] )
    C = Counter(list(''.join(Face)))
    win = sum(num-min_coin+1 for num in C.values() if num >= min_coin)
    if tuple(pnt) in Pnt:
        break
    ans += win
    Win.append(win)
    Pnt.append(tuple(pnt))

# analyze the repeat to sum additional wins
if len(Win) != ix+1:
    ix_rep = Pnt.index(tuple(pnt))
    len_rep = ix-ix_rep
    # add complete repeats
    num_rep = (n-ix) // len_rep
    ans += num_rep * sum(Win[ix_rep:])
    # add the last partial repeat
    ans += sum( Win[ ix_rep : ix_rep+n-ix-len_rep*num_rep ] )
print(ans)

