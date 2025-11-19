import sys

# parsing
X = [int(l.strip()) for l in open(sys.argv[1], 'r')]

# constraints
n_trn = 2025

# make the dial
Dial = [1] + \
[X[i] for i in range(len(X)) if i % 2 == 0] + \
[X[i] for i in range(len(X)) if i % 2 != 0][::-1]

# turn the dial
ans = Dial[(0 + n_trn) % len(Dial)]
print(ans)

