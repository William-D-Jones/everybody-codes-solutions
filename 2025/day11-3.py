import sys

# parsing
X = [int(l) for l in open(sys.argv[1], 'r')]

# We make the following simplifying assumptions and observations:
# (i) The list is sorted in strictly ascending order.
assert all(X[i+1] > X[i] for i in range(len(X)-1))
# (i-a) Therefore, we skip the first phase.
# (i-b) Because the list is strictly ascending (no equal neighbors), after each
# round exactly 2 numbers experience a net change: the highest-indexed number 
# that equals the minimum in the list, and the lowest-indexed number that 
# equals the maximum in the list.
# (i-c) Since exactly 2 numbers change with each round, we simply compute the
# final size of each column of ducks, take the difference of each number from
# the final size, and divide by 2.

sz = sum(X) // len(X) # the final size of each bin
ans = sum( abs( x - sz ) for x in X ) // 2
print(ans)

