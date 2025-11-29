import sys
import re
from collections import Counter

# parsing
X = open(sys.argv[1], 'r').read().strip().split('\n\n')
Pl = {} # gives the thickness of each plant
Br = {} # gives the thickness of each branch
for x in X:
    for i,xs in enumerate(x.split('\n')):
        if i == 0:
            # extract the thickness of the main plant
            M_plant = re.match(r'^Plant ([0-9]+) with thickness ([0-9]+):$', xs)
            src = int(M_plant.group(1))
            Pl[ src ] = int(M_plant.group(2))
        else:
            # extract the thickness of the branches
            M_free = re.match(r'^- free branch with thickness ([0-9]+)$', xs)
            M_con = re.match(\
            r'- branch to Plant ([0-9]+) with thickness ([0-9]+)$', xs)
            assert M_free or M_con
            if M_free:
                Br[(src,)] = int(M_free.group(1))
            elif M_con:
                tar = int(M_con.group(1))
                Br[ tuple(sorted([src,tar])) ] = int(M_con.group(2))

# setup a dictionary of energy to be delivered to each plant
En = Counter()
for br in Br.keys():
    if len(br) == 1:
        En[ br[0] ] += 1 * Br[br]
# energize target branches
Seen = set([br for br in Br.keys() if len(br) == 1])
while any(en > 0 for en in En.values()):
    En_Next = Counter()
    for src,en in En.items():
        # identify the branches stemming from the source plant
        Br_Next = [br for br in Br.keys() if src in br and br not in Seen]
        if len(Br_Next) == 0:
            ans = en if en >= Pl[src] else 0
            break
        for br in Br_Next:
            Seen.add( br )
            # identify the next target plant
            tar = [pl for pl in br if pl != src]
            assert len(tar) == 1
            tar = tar.pop()
            # determine the energy to be delivered
            en_next = (en * Br[br]) if en >= Pl[src] else 0
            En_Next[ tar ] += en_next
    En = En_Next
print(ans)

