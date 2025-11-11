import sys

KN = ['A']
NOV = ['a']

# parsing
X = list(open(sys.argv[1], 'r').read().strip())

ans = 0
for i in range(len(NOV)):
    Nov = [j for j in range(len(X)) if X[j] == NOV[i]]
    Kn = [j for j in range(len(X)) if X[j] == KN[i]]
    for nov in Nov:
        ans += len([j for j in Kn if j < nov])
print(ans)

