import sys
from collections import defaultdict

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

# check if the names are valid
Poss = []
for ix,name in enumerate(Name):
    if is_valid_name(name, Rule):
        Poss.append(''.join(name))
assert len(Poss) == 1
ans = Poss.pop()
print(ans)

