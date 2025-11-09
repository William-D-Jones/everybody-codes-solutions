import sys

D = {'U': (0,1,0), 'D': (0,-1,0), 'L': (-1,0,0), 'R': (1,0,0), 'F': (0,0,1), \
'B': (0,0,-1)}

# parsing
X = [l.strip() for l in open(sys.argv[1], 'r')]
Plant = []
for x in X:
    Plant.append([ ( inst[0], int(inst[1:]) ) for inst in x.split(',') ])

S = set()
for plant in Plant:
    x,y,z = 0,0,0
    for inst in plant:
        dx,dy,dz = D[inst[0]]
        n = inst[1]
        for _ in range(n):
            x,y,z = x+dx,y+dy,z+dz
            S.add( (x,y,z) )
ans = len(S)
print(ans)

