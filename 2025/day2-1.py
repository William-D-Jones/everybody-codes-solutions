import sys
import re

def op(I1, I2, oper):
    x1,y1 = I1
    x2,y2 = I2
    if oper == '+':
        R = (x1+x2, y1+y2)
    elif oper == '*':
        R = (x1 * x2 - y1 * y2, x1 * y2 + y1 * x2)
    elif oper == '/':
        R = ( int(x1/x2), int(y1/y2) )
    else:
        assert False
    return R

# parsing
X = [l.strip() for l in open(sys.argv[1], 'r')]
Var = {}
for x in X:
    M = re.match('^([A-Z]+)=\\[([0-9]+),([0-9]+)\\]$', x)
    var = M.group(1)
    x = int(M.group(2))
    y = int(M.group(3))
    Var[var] = (x,y)

R = (0,0)
for _ in range(3):
    R = op(R, R, '*')
    R = op(R, (10,10), '/')
    R = op(R, Var['A'], '+')
ans = '[' + ','.join(str(r) for r in R) + ']'
print(ans)

