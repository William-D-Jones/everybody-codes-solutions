import sys

# parsing
X = [int(l) for l in open(sys.argv[1], 'r')]

# constraints
max_rnd = 10

rnd = 0
while rnd < max_rnd and any(X[i+1] < X[i] for i in range(len(X)-1)):
    rnd += 1
    for i in range(len(X)-1):   
        if X[i+1] < X[i]:
            X[i] -= 1
            X[i+1] += 1
while rnd < max_rnd and any(X[i+1] > X[i] for i in range(len(X)-1)):
    rnd += 1
    for i in range(len(X)-1):   
        if X[i+1] > X[i]:
            X[i] += 1
            X[i+1] -= 1
ans = sum( (i+1)*x for i,x in enumerate(X) )
print(ans)

