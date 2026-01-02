import sys

def pop_balloon(ix_pop, n_tot, Balloon):
    if ix_pop in Balloon:
        ix_last, ix_next = Balloon[ix_pop]
        Balloon.pop(ix_pop)
    else:
        ix_last = (ix_pop-1) % n_tot
        ix_next = (ix_pop+1) % n_tot
    if ix_last in Balloon:
        Balloon[ix_last] = (Balloon[ix_last][0], ix_next)
    else:
        Balloon[ix_last] = ((ix_last-1) % n_tot, ix_next)
    if ix_next in Balloon:
        Balloon[ix_next] = (ix_last, Balloon[ix_next][1])
    else:
        Balloon[ix_next] = (ix_last, (ix_next+1) % n_tot)
    return ix_next, Balloon

# parsing
X = list(open(sys.argv[1], 'r').read().strip())

# constraints
n_rep = 100000
Bolt = ['R', 'G', 'B']

ix0 = 0 # index of the current balloon
ix1 = (len(X) * n_rep) // 2 # index of the opposite balloon
pnt = 0 # pointer to the current bolt
n_tot = len(X) * n_rep # original number of elements in the circle
n_cur = len(X) * n_rep # current number of elements in the circle
Balloon = {}
ans = 0
while n_cur > 0:
    ans += 1
    # identify the current and opposite balloons
    b0 = X[ ix0%len(X) ]
    b1 = X[ ix1%len(X) ]
    # pop the current balloon
    ix0, Balloon = pop_balloon(ix0, n_tot, Balloon)
    # pop the opposite balloon
    if n_cur % 2 == 0:
        if b0 == Bolt[pnt]:
            ix1, Balloon = pop_balloon(ix1, n_tot, Balloon)
            n_cur -= 2
        else:
            n_cur -= 1
    else:
        n_cur -= 1
        if ix1 in Balloon:
            ix1 = Balloon[ix1][1]
        else:
            ix1 = (ix1+1) % n_tot
    pnt = (pnt+1) % len(Bolt)
print(ans)        

