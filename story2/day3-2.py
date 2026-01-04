import sys
import re

def roll(ix, Face, seed, pulse, ix_roll, ix_last):
    spin = ix_roll * pulse
    ix_next = (ix_last + spin) % len(Face)
    pulse += spin
    pulse %= seed
    pulse += 1 + ix_roll + seed
    return ix_next, pulse

# parsing
X0, X1 = open(sys.argv[1], 'r').read().strip().split('\n\n')
Dice = []
for x in X0.split('\n'):
    M = re.match(r'^([0-9]+): faces=\[([0-9,\-]+)\] seed=([0-9]+)$', x)
    Dice.append( (int(M.group(1)), tuple(map(int,M.group(2).split(','))),
    int(M.group(3)) ) )
Track = tuple(map(int, list(X1)))

Pos = {ix: 0 for ix, Face, seen in Dice}
Win = []
Pulse = {ix: seed for ix, Face, seed in Dice}
Last = {ix: 0 for ix, Face, seed in Dice}
ix_roll = 0
while len(Win) < len(Dice):
    ix_roll += 1
    for ix, Face, seed in Dice:
        last = Last[ix]
        pulse = Pulse[ix]
        Last[ix], Pulse[ix] = roll(ix, Face, seed, Pulse[ix], ix_roll, Last[ix])
        if Pos[ix] < len(Track) and Face[ Last[ix] ] == Track[ Pos[ix] ]:
            Pos[ix] += 1
            if Pos[ix] == len(Track):
                Win.append(ix)
ans = ','.join(map(str,Win))
print(ans)

