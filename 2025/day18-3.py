import sys
import re

def energize(Start, Pl, Br):
    # setup a dictionary of energy to be delivered to each plant
    En = {}
    for br in Br.keys():
        if len(br) == 1:
            if br[0] not in En:
                En[ br[0] ] = 0
            if br in Start:
                En[ br[0] ] += 1 * Br[br]
    # energize target branches
    Seen = set([br for br in Br.keys() if len(br) == 1])
    while any(en > 0 for en in En.values()):
        En_Next = {}
        for src,en in En.items():
            # identify the branches stemming from the source plant
            Br_Next = [br for br in Br.keys() if src in br and br not in Seen]
            if len(Br_Next) == 0:
                return en if en >= Pl[src] else 0
            for br in Br_Next:
                Seen.add( br )
                # identify the next target plant
                tar = [pl for pl in br if pl != src]
                assert len(tar) == 1
                tar = tar.pop()
                # determine the energy to be delivered
                en_next = (en * Br[br]) if en >= Pl[src] else 0
                if tar not in En_Next:
                    En_Next[ tar ] = 0
                En_Next[ tar ] += en_next
        En = En_Next
    return 0

# parsing
X,T = open(sys.argv[1], 'r').read().strip().split('\n\n\n')
Pl = {} # gives the thickness of each plant
Br = {} # gives the thickness of each branch
for x in X.split('\n\n'):
    for i,xs in enumerate(x.split('\n')):
        if i == 0:
            # extract the thickness of the main plant
            M_plant = \
            re.match(r'^Plant ([0-9]+) with thickness ([0-9\-]+):$', xs)
            src = int(M_plant.group(1))
            Pl[ src ] = int(M_plant.group(2))
        else:
            # extract the thickness of the branches
            M_free = re.match(r'^- free branch with thickness ([0-9\-]+)$', xs)
            M_con = re.match(\
            r'- branch to Plant ([0-9]+) with thickness ([0-9\-]+)$', xs)
            assert M_free or M_con
            if M_free:
                Br[(src,)] = int(M_free.group(1))
            elif M_con:
                tar = int(M_con.group(1))
                Br[ tuple(sorted([src,tar])) ] = int(M_con.group(2))
Test = [ list(map(int,t.split())) for t in T.split('\n') ]

# We need to find the maximum energy achievable by the system. We make the 
# following observations:
# (i) With a simulation, we can find the identity of the final plant.
En = set([br[0] for br in Br.keys() if len(br) == 1])
Seen = set([br for br in Br.keys() if len(br) == 1])
T = set()
while En:
    En_Next = set()
    for src in En:
        Br_Next = [br for br in Br.keys() if src in br and br not in Seen]
        if len(Br_Next) == 0:
            T.add( src )
        for br in Br_Next:
            Seen.add( br )
            tar = [pl for pl in br if pl != src]
            assert len(tar) == 1
            tar = tar.pop()
            En_Next.add(tar)
    En = En_Next
assert len(T) == 1
T = T.pop()
# (ii) All branches with negative thickness project from one of the plants with
# a free branch. Consider the plants that are the targets of these negative
# branches, which we denote Pl_Neg.
Pl_Free = set([br[0] for br in Br.keys() if len(br) == 1])
Br_Neg = [br for br,th in Br.items() if th < 0]
assert all(br[0] in Pl_Free or br[1] in Pl_Free for br in Br_Neg)
Pl_Neg = set(br[0] if br[0] not in Pl_Free else br[1] for br in Br_Neg)
# (iii) Consider the plants that are the targets of the negative branches 
# (Pl_Neg). Since each of these plants receives input from only plants with
# free branches (with thickness 1 and energy input 1), we can compute the 
# maximum input to each plant in Pl_Neg by summing the thicknesses of its
# positive input branches only. Notably, many of these branches cannot be
# energized regardless of input.
Pl_Neg_En = set()
for pl in Pl_Neg:
    Br_In = \
    [br for br in Br.keys() if pl in br and any(plf in br for plf in Pl_Free)]
    en_max = sum(Br[br] for br in Br_In if Br[br] > 0)
    if en_max >= Pl[pl]:
        Pl_Neg_En.add(pl)
# (iv) Consider only the plants in Pl_Neg_En that can be energized. Each of 
# these plants receives input from positive and negative branches from free 
# plants. No free plant has a positive input to one plant in Pl_Neg_En and a
# negative input to another.
Pl_Free_Pos = set()
Pl_Free_Neg = set()
for pl in Pl_Neg_En:
    Br_In = \
    [br for br in Br.keys() if pl in br and any(plf in br for plf in Pl_Free)]
    for br in Br_In:
        src = [plf for plf in br if plf in Pl_Free]
        assert len(src) == 1
        src = src.pop()
        if Br[br] < 0:
            Pl_Free_Neg.add(src)
        elif Br[br] > 0:
            Pl_Free_Pos.add(src)
assert len(Pl_Free_Pos & Pl_Free_Neg) == 0
# (v) Each plant in Pl_Neg projects to exactly one other plant, and each one
# of these penultimate target plants projects to the terminus.
Br_Pen = [br for br in Br.keys() if len(br) > 1 and \
((br[0] in Pl_Neg or br[1] in Pl_Neg) and \
br[0] not in Pl_Free and br[1] not in Pl_Free)]
Pl_Pen = set(br[0] if br[0] not in Pl_Neg else br[1] for br in Br_Pen)
assert all(len([br for br in Br_Pen if pl in br])==1 for pl in Pl_Neg)
assert all(tuple(sorted([pl,T])) in Br for pl in Pl_Pen)
# (vi) Therefore, to achieve the maximum energy, simply turn on the plants in
# Pl_Free_Pos and turn off the plants in Pl_Free_Neg.
Start = [(pl,) for pl in Pl_Free_Pos]
en_max = energize(Start, Pl, Br)

# run test cases
ans = 0
for test in Test:
    Start = []
    for i,do in enumerate(test):
        if do == 1:
            Start.append( (i+1,) )
        else:
            assert do == 0
    en = energize(Start, Pl, Br)
    if en > 0:
        ans += (en_max - en)
print(ans)

