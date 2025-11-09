import sys
from collections import deque

D = {'U': (0,1,0), 'D': (0,-1,0), 'L': (-1,0,0), 'R': (1,0,0), 'F': (0,0,1), \
'B': (0,0,-1)}

# parsing
X = [l.strip() for l in open(sys.argv[1], 'r')]
Plant = []
for x in X:
    Plant.append([ ( inst[0], int(inst[1:]) ) for inst in x.split(',') ])

# identify all segments and leaves in the tree
L = set()
S = set()
for plant in Plant:
    x,y,z = 0,0,0
    for inst in plant:
        dx,dy,dz = D[inst[0]]
        n = inst[1]
        for _ in range(n):
            x,y,z = x+dx,y+dy,z+dz
            S.add( (x,y,z) )
    L.add( (x,y,z) )

# identify the main trunk, which proceeds immediately upward from (0,0,0)
T = set()
x,y,z = D['U']
dx,dy,dz = D['U']
while (x,y,z) in S:
    T.add( (x,y,z) )
    x,y,z = x+dx,y+dy,z+dz

# from each starting point, calculate the minimum distance to the leaves
Path = {(x,y,z): 0 for (x,y,z) in T}
for (tx,ty,tz) in T:
    dist_min_tot = 0
    for (lx,ly,lz) in L:
        Q = deque([ [ (tx,ty,tz), set([(tx,ty,tz)]), 0 ] ])
        Dist = {(tx,ty,tz): 0}
        while Q:
            (x,y,z), Seen, dist = Q.popleft()
            for dx,dy,dz in D.values():
                nx,ny,nz = x+dx,y+dy,z+dz
                if (nx,ny,nz) not in S or (nx,ny,nz) in Seen:
                    continue
                dist_next = dist + 1
                if (nx,ny,nz) not in Dist:
                    Dist[ (nx,ny,nz) ] = dist_next
                else:
                    if Dist[ (nx,ny,nz) ] <= dist_next:
                        continue
                    else:
                        Dist[ (nx,ny,nz) ] = dist_next
                if (nx,ny,nz) != (lx,ly,lz):
                    Q.append( \
                    [ (nx,ny,nz), Seen | set( (nx,ny,nz) ), dist_next ] \
                    )
        Path[ (tx,ty,tz) ] += Dist[ (lx,ly,lz) ]
ans = min(Path.values())
print(ans)

