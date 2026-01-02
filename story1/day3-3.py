import sys
import re
import math

def get_euclid_ext(a, b):
    R = [a, b]
    S = [1, 0]
    T = [0, 1]
    while R[-1] != 0:
        i = len(R)-1
        q = R[-2] // R[-1]
        R.append( R[-2] - q * R[-1] )
        S.append( S[-2] - q * S[-1] )
        T.append( T[-2] - q * T[-1] )
    return R[-2], S[-2], T[-2]

def crt(r0, m0, r1, m1):
    g, s, t = get_euclid_ext(m0, m1)
    assert g == 1
    return r0 * t * m1 + r1 * s * m0

# parsing
X = [line.strip() for line in open(sys.argv[1], 'r')]
Coord = []
for x in X:
    M = re.match(r'^x=([0-9]+) y=([0-9]+)', x)
    Coord.append( (int(M.group(1)), int(M.group(2))) )

# For a given coordinate (c,r), the snail arrives on the golden line every
# (c+r-1) days on or after day r-1. Let n_day be the number of days required 
# for each snail to arrive at the golden line. Then:
# n_day - (r-1) % (c+r-1) = 0
# n_day % (c+r-1) = r-1
# First, calculate the remainder and modulus associated with each snail:
Rem = [r-1 for (c,r) in Coord]
Mod = [c+r-1 for (c,r) in Coord]
# Next, apply the Chinese Remainder Theorem to the snails:
ix = 1
m0 = Mod[0]
r0 = Rem[0]
while ix<len(Coord):
    m1 = Mod[ix]
    r1 = Rem[ix]
    r0 = crt(r0, m0, r1, m1)
    m0 = m0 * m1
    ix += 1
ans = r0 % math.prod(Mod)
print(ans)

