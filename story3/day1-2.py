import sys

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

max_shine = max(col['s'] for col in Col.values())
Dark = {ix: col['r'] + col['g'] + col['b'] for ix, col in Col.items()}
min_col = min(Dark[ix] for ix, col in Col.items() if col['s'] == max_shine)
min_ix = \
[ix for ix, col in Col.items() if col['s'] == max_shine and Dark[ix] == min_col]
assert len(min_ix) == 1
ans = min_ix[0]
print(ans)
