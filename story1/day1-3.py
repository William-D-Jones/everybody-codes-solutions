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
    if len(Rem)==e:
        res = sum(Rem)
    else:
        ix_rep = Rem.index(score)
        len_rep = len(Rem)-ix_rep
        n_rep = (e-1-ix_rep) // len_rep
        ix_last = ix_rep + (e-1-ix_rep-len_rep*n_rep)
        sum_pre = sum(Rem[:ix_rep])
        sum_rep = sum(Rem[ix_rep:]) * n_rep
        sum_post = sum(Rem[ix_rep:ix_last+1])
        res = sum_pre + sum_rep + sum_post
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

