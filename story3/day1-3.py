import sys
from collections import Counter

a = ord('a')
z = ord('z')
A = ord('A')
Z = ord('Z')

# parsing
X = [l.strip().split(':') for l in open(sys.argv[1], 'r')]
Col = {}
for sc, scol in X:
    ix = int(sc)
    Col[ix] = {}
    for col in scol.split(' '):
        assert all(\
        let in ('r', 'R', 'g', 'G', 'b', 'B', 's', 'S') for let in col)
        nm = col[0] if a <= ord(col[0]) <= z else chr(ord(col[0]) - A + a)
        val = ''.join(tuple('0' if a <= ord(let) <= z else '1' for let in col))
        Col[int(ix)][nm] = int(val, 2)

RGB = ('r', 'g', 'b')
Grp_Num = Counter()
Grp_Tot = Counter()
for sc, col in Col.items():
    if col['s'] <= 30:
        grp_shine = 'matte'
    elif col['s'] >= 33:
        grp_shine = 'shiny'
    else:
        grp_shine = ''
    top_col = []
    for col1 in RGB:
        if all(col[col1] > col[col2] or col1 == col2 for col2 in RGB):
            top_col.append(col1)
    if len(top_col) == 1 and grp_shine != '':
        top_col = top_col.pop()
        Grp_Num[top_col + '-' + grp_shine] += 1
        Grp_Tot[top_col + '-' + grp_shine] += sc
max_grp = [grp for grp, tot in Grp_Num.items() if tot == max(Grp_Num.values())]
assert len(max_grp) == 1
max_grp = max_grp.pop()
ans = Grp_Tot[max_grp]
print(ans)
