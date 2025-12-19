import sys

# parsing
X0, X1 = open(sys.argv[1], 'r').read().strip().split('\n\n')
Turn = list(map(int, X0.split(',')))
Wheel = [[] for turn in Turn]
nchar = 3
for x in X1.split('\n'):
    Face = [ x[ (nchar+1)*i : (nchar+1)*i+nchar ] for \
    i in range( (len(x)+1) // (nchar+1) )]
    for i,face in enumerate(Face):
        if face != ' '*nchar:
            Wheel[i].append(face)

# constraints
n = 100

Face = []
for i,turn in enumerate(Turn):
    Face.append( Wheel[i][ n * turn % len(Wheel[i]) ] )
ans = ' '.join(Face)
print(ans)

