import sys

# parsing
X = [l.strip() for l in open(sys.argv[1], 'r')]
Conv = {}
for x in X:
    tin, tout = x.split(':')
    Conv[tin] = list(tout.split(','))

T = ['A']
for _ in range(4):
    T_Next = []
    while T:
        t = T.pop(0)
        T_Next += Conv[t]
    T = T_Next
ans = len(T)
print(ans)

