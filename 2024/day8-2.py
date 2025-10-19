import sys
from collections import Counter

# parsing
X = int(open(sys.argv[1], 'r').read().strip())

# constraints
n_aco = 1111
n_blk = 20240000

# build the structure
th = 1
ix = 1
min_x = 0
max_x = 0
Col = Counter()
while n_blk > 0:
    if ix == 1:
        # place the first block
        Col[0] += 1
        n_blk -= 1
    else:
        # place blocks on extant columns until the thickness is achieved
        n_th = 0
        while n_th < th:
            # add to the columns
            for col in range(min_x,max_x+1):
                Col[col] += 1
                n_blk -= 1
            # place the left- and right-hand blocks
            if n_th == 0:
                Col[min_x-1] += 1
                Col[max_x+1] += 1
                min_x -= 1
                max_x += 1
                n_blk -= 2
            n_th += 1
    # get the thickness of the next layer
    ix += 1
    th = (th * X) % n_aco

# calculate the final width
w = max_x - min_x + 1
ans = w * -1 * n_blk
print(ans)

