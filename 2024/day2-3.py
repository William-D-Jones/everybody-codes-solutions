import sys

D = [ (0,1), (1,0), (0,-1), (-1,0) ]

# parsing
X = open(sys.argv[1], 'r').read().strip()
X1,X2 = X.split('\n\n')
W = X1[ len('WORDS:') : ].split(',')
I = X2.split('\n')
nrow = len(I)
ncol = len(I[0])

# part 3
S = set()
for r in range(nrow):
    for c in range(ncol):
        print(r,nrow,c,ncol)
        for w in W:
            n = len(w)
            for dr,dc in D:
                ir,ic = r,c
                set_test = set()
                str_test = ''
                for _ in range(n):
                    str_test += I[ir][ic]
                    set_test.add( (ir,ic) )
                    ir = ir+dr
                    if not 0<=ir<nrow:
                        break
                    ic = (ic+dc) % ncol
                    if not w.startswith(str_test):
                        break
                if str_test == w:
                    S |= set_test
ans = len(S)
print(ans)

