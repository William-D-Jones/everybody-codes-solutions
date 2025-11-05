import sys
import re

# parsing
X0,X1 = open(sys.argv[1], 'r').read().strip().split('\n\n')
Name = list(X0.split(','))
Inst = []
for x1 in X1.split(','):
    M = re.match('^([RL])([0-9]+)', x1)
    Inst.append( (M.group(1), int(M.group(2))) )

pnt = 0
for dx,n in Inst:
    if dx == 'R':
        pnt = min(pnt+n, len(Name))
    elif dx == 'L':
        pnt = max(pnt-n, 0)
    else:
        assert False
ans = Name[pnt]
print(ans)
    
