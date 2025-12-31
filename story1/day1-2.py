import sys

def eni(n, e, m):
    Rem = []
    score = 1
    # simulate until we find a repeat
    for _ in range(e):
        score *= n
        score %= m
        if score not in Rem:
            Rem.append(score)
        else:
            break
    # analyze the repeats
    Res = []
    for i in range(5):
        ix_find = e-(i+1)
        if ix_find < 0:
            continue
        if ix_find < len(Rem):
            Res.append( Rem[ix_find] )
        else:
            ix_rep = Rem.index(score)
            len_rep = len(Rem)-ix_rep
            n_rep = (ix_find-ix_rep) // len_rep
            ix = ix_rep + (ix_find-ix_rep-len_rep*n_rep)
            Res.append( Rem[ix] )
    res = int(''.join(map(str,Res)))
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

