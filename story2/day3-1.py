import sys
import re

def roll(ix, Face, seed, pulse, ix_roll, ix_last):
    spin = ix_roll * pulse
    ix_next = (ix_last + spin) % len(Face)
    pulse += spin
    pulse %= seed
    pulse += 1 + ix_roll + seed
    return ix_next, pulse

# constraints
n_min = 10000

# parsing
X = [line.strip() for line in open(sys.argv[1], 'r')]
Dice = []
for x in X:
    M = re.match(r'^([0-9]+): faces=\[([0-9,\-]+)\] seed=([0-9]+)$', x)
    Dice.append( (int(M.group(1)), tuple(map(int,M.group(2).split(','))),
    int(M.group(3)) ) )

Pulse = {ix: seed for ix, Face, seed in Dice}
Last = {ix: 0 for ix, Face, seed in Dice}
ix_roll = 0
n_tot = 0
while n_tot < n_min:
    ix_roll += 1
    for ix, Face, seed in Dice:
        last = Last[ix]
        pulse = Pulse[ix]
        Last[ix], Pulse[ix] = roll(ix, Face, seed, Pulse[ix], ix_roll, Last[ix])
        n_tot += Face[ Last[ix] ]
ans = ix_roll
print(ans)

