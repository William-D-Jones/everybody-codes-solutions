import sys
from collections import Counter

# parsing
X = int(open(sys.argv[1], 'r').read().strip())

# constraints
n_aco = 10
n_blk = 202400000

# build the structure
th = 1
ix = 1
min_x = 0
max_x = 0
Col = Counter() # the height of each column
Blk = Counter() # the number of blocks in each column
while n_blk - sum(Blk.values()) > 0:
    if ix == 1:
        # place the first block
        Col[0] += 1
        Blk[0] += 1
    else:
        # place blocks on extant columns until the thickness is achieved
        n_th = 0
        while n_th < th:
            # add to the columns
            for col in range(min_x,max_x+1):
                Col[col] += 1
                Blk[col] += 1
            # place the left- and right-hand blocks
            if n_th == 0:
                Col[min_x-1] += 1
                Blk[min_x-1] += 1
                Col[max_x+1] += 1
                Blk[max_x+1] += 1
                min_x -= 1
                max_x += 1
            n_th += 1
    # empty the columns of unneeded blocks
    w = max_x - min_x + 1
    for col in range(min_x+1,max_x):
        n_empty = X * w * Col[col] % n_aco
        n_keep = Col[col] - n_empty
        Blk[col] = n_keep
    # get the thickness of the next layer
    ix += 1
    th = ( (th * X) % n_aco ) + n_aco

# calculate the final blocks needed
ans = sum(Blk.values()) - n_blk
print(ans)

