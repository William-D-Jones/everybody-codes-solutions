import sys

# parsing
X = [int(l) for l in open(sys.argv[1], 'r')]

ans = 0
while any(X[i+1] < X[i] for i in range(len(X)-1)):
    ans += 1
    for i in range(len(X)-1):   
        if X[i+1] < X[i]:
            X[i] -= 1
            X[i+1] += 1
while any(X[i+1] > X[i] for i in range(len(X)-1)):
    ans += 1
    for i in range(len(X)-1):   
        if X[i+1] > X[i]:
            X[i] += 1
            X[i+1] -= 1
print(ans)

