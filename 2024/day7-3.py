import sys
import itertools

D = [ (0,1), (1,0), (0,-1), (-1,0) ]

TRK = """\
S+= +=-== +=++=     =+=+=--=    =-= ++=     +=-  =+=++=-+==+ =++=-=-=--
- + +   + =   =     =      =   == = - -     - =  =         =-=        -
= + + +-- =-= ==-==-= --++ +  == == = +     - =  =    ==++=    =++=-=++
+ + + =     +         =  + + == == ++ =     = =  ==   =   = =++=
= = + + +== +==     =++ == =+=  =  +  +==-=++ =   =++ --= + =
+ ==- = + =   = =+= =   =       ++--          +     =   = = =--= ==++==
=     ==- ==+-- = = = ++= +=--      ==+ ==--= +--+=-= ==- ==   =+=    =
-               = = = =   +  +  ==+ = = +   =        ++    =          -
-               = + + =   +  -  = + = = +   =        +     =          -
--==++++==+=+++-= =-= =-+-=  =+-= =-= =--   +=++=+++==     -=+=++==+++-\
"""

def run_track(Act, Trk, num_loop, start_pwr):
    pwr = start_pwr
    ess = 0
    n_seg = num_loop * len(Trk)
    for ix in range(n_seg):
        act = Act[ix % len(Act)]
        trk = Trk[ix % len(Trk)]
        if trk == '+':
            pwr += 1
        elif trk == '-' and pwr >= 1:
            pwr -= 1
        elif trk == '-' and pwr < 1:
            pass
        elif trk == '=' or trk == 'S':
            if act == '+':
                pwr += 1
            elif act == '-' and pwr >= 1:
                pwr -= 1
            elif act == '-' and pwr < 1:
                pass
            elif act == '=':
                pass
            else:
                assert False
        else:
            assert False
        ess += pwr
    return ess

# parsing actions
X = [ list(l.strip().split(':')) for l in open(sys.argv[1], 'r') ]
Act = {}
for x in X:
    Act[ x[0] ] = tuple(x[1].split(','))
Act = list(Act.values())
assert len(Act) == 1
Act = Act.pop()

# parsing track
TRKS = [list(row) for row in TRK.split('\n')]
nrow = len(TRKS)
ncol = max(len(row) for row in TRKS)
for r in range(len(TRKS)):
    while len(TRKS[r]) < ncol:
        TRKS[r].append(' ')
Trk = []
r,c = 0,0
dr,dc = 0,1
while len(Trk) == 0 or TRKS[r][c] != 'S':
    r += dr
    c += dc
    Trk.append( TRKS[r][c] )
    for drn,dcn in D:
        if (drn != -dr or dcn != -dc) and 0<=r+drn<nrow and 0<=c+dcn<ncol and \
        TRKS[r+drn][c+dcn] != ' ':
            dr = drn
            dc = dcn
            break

# constraints
num_loop = 2024
num_plan = 11
num_pl = 5
num_mi = 3
start_pwr = 10

# get the essence achieved by the opponent knight
ess_op = run_track(Act, Trk, num_loop, start_pwr)

# loop through possible plans to defeat the opponent
ans = 0
S = set(range(num_plan))
for com_pl in itertools.combinations(S, num_pl):
    S_Mi = S - set(com_pl)
    for com_mi in itertools.combinations(S_Mi, num_mi):
        Plan = []
        for i in range(num_plan):
            if i in com_pl:     
                Plan.append('+')
            elif i in com_mi:
                Plan.append('-')
            else:
                Plan.append('=')
        ess_plan = run_track(Plan, Trk, num_loop, start_pwr)
        if ess_plan > ess_op:
            ans += 1
print(ans)
        
