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

def is_engrave(X):
    R = (0,0)
    out = True
    for _ in range(100):
        R = op(R, R, '*')
        R = op(R, (100000,100000), '/')
        R = op(R, X, '+')
        if not all(-1000000 <= c <= 1000000 for c in R):
            out = False
            break
    return out

# parsing
X = [l.strip() for l in open(sys.argv[1], 'r')]
Var = {}
for x in X:
    M = re.match('^([A-Z]+)=\\[([0-9\\-]+),([0-9\\-]+)\\]$', x)
    var = M.group(1)
    x = int(M.group(2))
    y = int(M.group(3))
    Var[var] = (x,y)

# get the coordinates of the top left and bottom right corners
xmin,ymin = Var['A']
xmax,ymax = op(Var['A'], (1000,1000), '+')
xlen = xmax-xmin+1
ylen = ymax-ymin+1

# divide up the grid and test points
Eng = set()
xtest,ytest = Var['A']
glen = 101
dx = (xlen-1) // (glen-1)
dy = (ylen-1) // (glen-1)
for gy in range(glen):
    for gx in range(glen):
        if is_engrave( (xtest,ytest) ):
            Eng.add( (xtest,ytest) )
        xtest += dx
    ytest += dy
    xtest = Var['A'][0]
ans = len(Eng)
print(ans)

