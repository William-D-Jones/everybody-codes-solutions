import sys
import math

# parsing
X = int(open(sys.argv[1], 'r').read().strip())

# the number of blocks in the kth layer is the kth odd number
# the sum of the odd numbers from 1 to n is given by S=n**2

# to solve, find the smallest n such that n**2 >= X (the input)
n = math.ceil(X**0.5)
# get the width of the base
w = 2*n-1
# get the missing blocks
m = n**2 - X
# get the final answer
ans = w*m
print(ans)

