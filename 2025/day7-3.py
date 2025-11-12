import sys
from collections import defaultdict, deque

def is_valid_name(N, Rule):
    for i in range(len(name)-1):
        char = name[i]
        char_next = name[i+1]
        if char_next not in Rule[char]:
            return False
    return True

# parsing
X1, X2 = open(sys.argv[1], 'r').read().strip().split('\n\n')
Name = list(map(list,X1.split(',')))
Rule = defaultdict(set)
for x in X2.split('\n'):
    s_in, s_out = x.split(' > ')
    Rule[s_in] |= set(s_out.split(','))

# constraints
n_min = 7
n_max = 11

# check if the prefixes are valid
Poss = []
for ix,name in enumerate(Name):
    if is_valid_name(name, Rule):
        Poss.append(name)

# drop redundant prefixes, which ensures all names are unique
Uni = []
while Poss:
    name0 = Poss.pop()
    if all(name0[:len(name1)] != name1 for name1 in Poss) and \
    len(name0) <= n_max:
        Uni.append(name0)

# construct names
ans = 0
Q = deque([ (name[-1],len(name)) for name in Uni ])
while Q:
    char,n_char = Q.popleft()
    n_char += 1
    for char_next in Rule[char]:
        if n_min <= n_char <= n_max:
            ans += 1
        if n_char < n_max:
            Q.append( (char_next,n_char) )
print(ans)

