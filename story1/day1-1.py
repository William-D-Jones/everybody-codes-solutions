import sys

def eni(n, e, m):
    Rem = []
    score = 1
    for _ in range(e):
        score *= n
        score %= m
        Rem.append(score)
    res = int(''.join(map(str,Rem[::-1])))
    return res

# parsing
X = [line.strip().split(' ') for line in open(sys.argv[1], 'r')]
Par = []
for x in X:
    par = {}
    for entry in x:
        var,val = entry.split('=')
        par[var] = int(val)
    Par.append(par)

ans = 0
for par in Par:
    res = eni(par['A'], par['X'], par['M']) + \
    eni(par['B'], par['Y'], par['M']) + eni(par['C'], par['Z'], par['M'])
    ans = max(ans, res)
print(ans)

