import sys
import functools

# parsing
X = [l.strip() for l in open(sys.argv[1], 'r')]
CONV = {}
for x in X:
    tin, tout = x.split(':')
    CONV[tin] = list(tout.split(','))

@functools.cache
def evolve(t, nday):
    if nday == 0:
        return 1
    else:
        return sum(evolve(t_next, nday-1) for t_next in CONV[t])

NT = []
for t in CONV.keys():
    nt = evolve(t, 20)
    NT.append(nt)
ans = max(NT) - min(NT)
print(ans)

