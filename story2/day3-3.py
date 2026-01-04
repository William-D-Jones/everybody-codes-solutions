import sys
import re
from collections import deque

D = [(0,1), (1,0), (0,-1), (-1,0), (0,0)]

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
Grid = [list(map(int,row.strip())) for row in X1.split('\n')]
nrow = len(Grid)
ncol = len(Grid[0])
assert all(len(row)==ncol for row in Grid)

# roll the dice once, identifying starting positions for the players
Pulse = {ix: seed for ix, Face, seed in Dice}
Last = {ix: 0 for ix, Face, seed in Dice}
ix_roll = 1
for ix, Face, seed in Dice:
    last = Last[ix]
    pulse = Pulse[ix]
    Last[ix], Pulse[ix] = \
    roll(ix, Face, seed, Pulse[ix], ix_roll, Last[ix])
# setup the possible starting positions in a queue
Coin = { (r,c) for r in range(nrow) for c in range(ncol) }
Seen = set()
Q = deque()
n_won = 0
for r in range(nrow):
    for c in range(ncol):
        for ix, Face, seen in Dice:
            if Face[ Last[ix] ]==Grid[r][c]:
                Q.append( ((r,c), ix, 1) )
                Seen.add( ((r,c), ix, 1) )
                if (r,c) in Coin:
                    Coin.remove( (r,c) )
                    n_won += 1
# simulate rolls until all possible paths are identified
while Q and Coin:
    (r,c), token, roll_last = Q.popleft()
    # update the dce if needed
    roll_next = roll_last + 1
    if ix_roll < roll_next:
        ix_roll += 1
        for ix, Face, seed in Dice:
            last = Last[ix]
            pulse = Pulse[ix]
            Last[ix], Pulse[ix] = \
            roll(ix, Face, seed, Pulse[ix], ix_roll, Last[ix])
    # move players to new squares
    for dr,dc in D:
        nr = r+dr
        nc = c+dc
        # check if the new coordinate is valid and unseen
        if not 0<=nr<nrow or not 0<=nc<ncol or \
        Grid[nr][nc] != Face[ Last[token] ] or \
        ((nr,nc), token, roll_next) in Seen:
            continue
        Seen.add( ((nr,nc), token, roll_next) )
        # check if a coin is available at the new coordinate
        if (nr,nc) in Coin:
            Coin.remove( (nr,nc) )
            n_won += 1
        # continue the journey
        Q.append( ((nr,nc), token, roll_next) )
ans = n_won
print(ans)

