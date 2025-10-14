import sys
import re

# parsing
X = open(sys.argv[1], 'r').read().strip()
X1,X2 = X.split('\n\n')
Words = X1[ len('WORDS:') : ].split(',')
Insc = X2.split('\n')
re_words = []
for word in Words:
    re_words.append(re.compile(word))

# part 2
ans = 0
for insc in Insc:
    Symbol = set()
    for i in range(len(insc)):
        for word in Words:
            if insc[i:].startswith(word):
                Symbol |= set(range(i, i+len(word)))
            if insc[i::-1].startswith(word):
                Symbol |= set( range(i, i-len(word), -1) )
    ans += len(Symbol)
print(ans)

