import sys

# parsing
X = [ list(l.strip().split(':')) for l in open(sys.argv[1], 'r') ]
Act = {}
for x in X:
    Act[ x[0] ] = tuple(x[1].split(','))

Pwr = { dev: 10 for dev in Act.keys() }
Ess = { dev: 0 for dev in Act.keys() }
n_seg = 10
for dev in Act.keys():
    for ix in range(n_seg):
        act = Act[dev][ix % len(Act[dev])]
        if act == '+':
            Pwr[dev] += 1
        elif act == '-' and Pwr[dev] >= 1:
            Pwr[dev] -= 1
        elif (act == '-' and Pwr[dev] < 1) or act == '=':
            pass
        else:
            assert False
        Ess[dev] += Pwr[dev]
Ess_Srt = sorted([(ess,dev) for dev,ess in Ess.items()])[::-1]
Ess_Rnk = [dev for ess,dev in Ess_Srt]
ans = ''.join(Ess_Rnk)
print(ans)

