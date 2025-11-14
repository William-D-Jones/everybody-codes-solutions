import sys
import itertools

# parsing
X = [l.strip().split(':') for l in open(sys.argv[1], 'r')]
Sc = {int(x[0]): list(x[1]) for x in X}

# find children and parents
Ch = {}
for ch,seq_ch in Sc.items():
    P = set(p for p in Sc.keys() if p != ch)
    for p0,p1 in itertools.combinations(P, 2):
        seq_p0 = Sc[p0]
        seq_p1 = Sc[p1]
        if all(seq_ch[i] == seq_p0[i] or seq_ch[i] == seq_p1[i] for \
        i in range(len(seq_ch))):
            if ch not in Ch:
                Ch[ch] = []
            Ch[ch].append(p0)
            Ch[ch].append(p1)
assert all(len(Ch[ch]) == 2 for ch in Ch.keys())
assert len(Ch) == 1

# get the degree of similarity
ans = 0
for ch in Ch.keys():
    seq_ch = Sc[ch]
    sim = 1
    for p in Ch[ch]:
        sim *= sum(1 for i in range(len(seq_ch)) if seq_ch[i] == Sc[p][i])
    ans += sim
print(ans)

