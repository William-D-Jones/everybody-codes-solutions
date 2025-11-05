import sys
import re

# parsing
X0,X1 = open(sys.argv[1], 'r').read().strip().split('\n\n')
Name = list(X0.split(','))
Inst = []
for x1 in X1.split(','):
    M = re.match('^([RL])([0-9]+)', x1)
    Inst.append( (M.group(1), int(M.group(2))) )

for dx,n in Inst:
    if dx == 'R':
        pnt = n % len(Name)
    elif dx == 'L':
        pnt = -n % len(Name)
    else:
        assert False
    Name[0],Name[pnt] = Name[pnt],Name[0]
ans = Name[0]
print(ans)
    
