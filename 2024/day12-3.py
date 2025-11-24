import sys
import math

# parsing
X = [tuple(map(int,l.strip().split())) for l in open(sys.argv[1], 'r')]

# constraints
num_height = 3

# We can make several observations regarding the problem. First, impose a 
# sensible coordinate system upon the grid: the A of the catapoult is defined
# as (0,0), using the format (r,c). We are given distances of each target 
# relative to A in the format (dc,dr), that is, (delta_column, delta_row).
# Next, define the absolute time of the collision as t, and
# the time of the collision relative to the projectile launch as t_proj. Then
# t = t_proj + dt, where dt is a time delay and dt >= 0. Finally, let seg be
# the number of the catapoult segment from which the projectile is launched,
# such that if the catapoult is launched from A, seg = 1. Let pwr be the power
# of the projectile.

# (i) We wish to hit each target at the highest altitude possible. Therefore,
# not all phases of the projectile are equally preferable. In particular, the 
# upslope of the projectile will be the best, since this allows us to freely
# increase the height without affecting the projectile path. Second-best is the
# projectile plateau, since we are not sacrificing any height. Worst is the 
# projectile downslope, since this requires us to lose height.

# (ii) After launch, the projectile always travels away from the catapoult at
# one unit per second. Therefore, the column of the collision is given by:
# C = dc - t = t_proj = t - dt
# Then:
# t = (dc + dt) / 2
# There exist many targets for which dc is odd. In this case, dt must also be
# odd to guarantee that t % 2 == 0. Therefore, dt % 2 == dc % 2.
# The row of the collision is more challenging to determine and depends on the
# projectile phase during which the collision occurs.

# (iii) Suppose we can hit the target during the projectile upslope. We can
# do this if the target path intersects the ground sufficiently close to the
# catapoult. The collision row is given by:
# R = dr - t = seg - 1 + t_proj = seg - 1 + t - dt
# Then:
# t = ( dr + dt - (seg - 1) ) / 2
# Substituting equation (ii):
# dc = dr - (seg - 1)
# seg = dr - dc + 1

# (iv) Suppose we can hit the target during the projectile plateau. The 
# collision row is given by:
# R = dr - t = seg - 1 + pwr
# Rearranging:
# seg + pwr = dr - t - 1
# Substituting equation (ii):
# seg + pwr = dr - ((dc+dt) / 2) - 1

# (v) Suppose we can hit the target during the projectile downslope. The
# collision row is given by:
# R = dr - t = seg - 1 + pwr - (t - dt - 2 * pwr) = seg - 1 + 3 * pwr - t + dt
# Rearranging:
# dr = (seg-1) + 3 * pwr + dt

ans = 0
for dc,dr in X:
    rnk = None
    # try a collision during the projectile upslope
    if 1 <= dr-dc+1 <= num_height:
        seg = dr-dc+1
        R = (seg-1 + dr) // 2
        pwr = R - (seg-1)
        # double check
        t = dr - R
        dt = seg - 1 + t - R
        assert t == math.ceil(dc/2)
        assert t-dt == dc-t and dr-t == seg-1 + (t-dt)
        if t-dt <= pwr:
            # calculate the rank
            if rnk is not None:
                rnk = min(rnk, seg * pwr)
            else:
                rnk = seg * pwr
    # try a collision during the projectile plateau
    # determine the sum of the segment and power if we have a plateau collision
    if dr - math.ceil( dc/2 ) > 0:
        t = math.ceil( dc/2 )
        dt = 0 if dc % 2 == 0 else 1
        R = dr - math.ceil( dc/2 )
        seg = max(1,dr-dc+1)
        pwr = R - (seg-1)
        while (seg+1) * (pwr-1) < seg * pwr and \
        seg+1 <= num_height and pwr-1 > 0:
            seg += 1
            pwr -= 1
        # double check
        assert t-dt == dc-t and dr-t == seg-1 + pwr
        if pwr < t-dt <= 2*pwr:
            # calculate the rank
            if rnk is not None:
                rnk = min(rnk, seg * pwr)
            else:
                rnk = seg * pwr
    # try a collision during the projectile downslope
    dt = 0 if dc % 2 == 0 else 1
    pwr = (dr - dt) // 3
    seg = dr - dt - 3 * pwr + 1
    if pwr > 0 and 1 <= seg <= num_height:
        while (seg+3) * (pwr-3) < seg * pwr and \
        1 <= seg+3 <= num_height and pwr-3 > 0:
            seg += 3
            pwr -= 3
        # double check
        t = (dc + dt) // 2
        assert t-dt == dc-t and dr-t == seg-1 + pwr - (t-dt-2*pwr)
        # calculate the rank
        if 2 * pwr < t-dt:
            if rnk is not None:
                rnk = min(rnk, seg * pwr)
            else:
                rnk = seg * pwr
    ans += rnk
print(ans)

