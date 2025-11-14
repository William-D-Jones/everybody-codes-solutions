import sys

# parsing
X = list(map(int,open(sys.argv[1], 'r').read().strip().split(',')))

# constraints
n_nail = 32

ans = 0
for i in range(len(X)-1):
    start = X[i]
    end = X[i+1]
    if end == (start + (n_nail // 2)) % n_nail:
        ans += 1
print(ans)

