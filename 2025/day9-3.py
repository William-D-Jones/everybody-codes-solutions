import sys
import itertools
from collections import deque

# parsing
X = [l.strip().split(':') for l in open(sys.argv[1], 'r')]
Sc = {int(x[0]): list(x[1]) for x in X}

# find children and parents
Ch = {}
for ch,seq_ch in Sc.items():
    P = set(p for p in Sc.keys() if p != ch)
    for p0,p1 in itertools.combinations(P, 2):
        seq_p0 = Sc[p0]
        seq_p1 = Sc[p1]
        if all(seq_ch[i] == seq_p0[i] or seq_ch[i] == seq_p1[i] for \
        i in range(len(seq_ch))):
            if ch not in Ch:
                Ch[ch] = []
            Ch[ch].append(p0)
            Ch[ch].append(p1)
assert all(len(Ch[ch]) == 2 for ch in Ch.keys())

# construct families
Orph = set(Sc.keys())
Fam = []
while Orph:
    # start a new family
    orph = Orph.pop()
    fam = set([orph])
    Q = deque([orph])
    # trace the new family
    while Q:
        duck = Q.popleft()
        # find the parents of the duck
        P_duck = Ch[duck] if duck in Ch else []
        for p in P_duck:
            if p not in fam:
                fam.add(p)
                Q.append(p)
                Orph.remove(p)
        # find the children of the duck
        Ch_duck = [ch for ch,P in Ch.items() if duck in P]
        for ch in Ch_duck:
            if ch not in fam:
                fam.add(ch)
                Q.append(ch)
                Orph.remove(ch)
    # store the new family
    Fam.append(fam)
ans = max(sum(fam) for fam in Fam)
print(ans)

