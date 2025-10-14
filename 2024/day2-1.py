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

# part 1
ans = 0
for r in re_words:
    ans += len( r.findall(Insc[0]) )
print(ans)

