import sys

# parsing
X = [int(x) for x in open(sys.argv[1], 'r').read().strip().split(',')]

S = set(X)
L = []
while len(S) > 0 and (len(L) == 0 or max(S) > max(L)):
    smin = min(S)
    L.append(smin)
    S.remove(smin)
ans = sum(L)
print(ans)

