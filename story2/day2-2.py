import sys

# parsing
X = list(open(sys.argv[1], 'r').read().strip())

# constraints
n_rep = 100
Bolt = ['R', 'G', 'B']

Balloon = X * n_rep
pnt = 0
ans = 0
while Balloon:
    ans += 1
    if Balloon[0]==Bolt[pnt] and len(Balloon) % 2 == 0:
        Balloon.pop(len(Balloon)//2)
    Balloon.pop(0)
    pnt = (pnt + 1) % len(Bolt)
print(ans)

