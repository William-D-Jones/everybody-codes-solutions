import sys
import re
from collections import Counter

# parsing
X = [line.strip() for line in open(sys.argv[1], 'r')]
Inst = []
for x in X:
    M = re.match(\
    r'^ADD id=([0-9]+) left=\[([0-9]+),(.+)\] right=\[([0-9]+),(.+)\]$', x)
    ix = int(M.group(1))
    rank_l = int(M.group(2))
    sym_l = M.group(3)
    rank_r = int(M.group(4))
    sym_r = M.group(5)
    Inst.append( (ix,rank_l,sym_l,rank_r,sym_r) )

# construct the tree
Tree = {}
for ix, rank_l, sym_l, rank_r, sym_r in Inst:
    for dx in (-1, 1):
        if dx==-1:
            rank, sym = rank_l, sym_l
        elif dx==1:
            rank, sym = rank_r, sym_r
        Pnt = [dx]
        while tuple(Pnt) in Tree:
            ix_i, rank_i, sym_i = Tree[tuple(Pnt)]
            if rank < rank_i:
                Pnt.append(-1)
            elif rank > rank_i:
                Pnt.append(1)
            else:
                assert False
        Tree[tuple(Pnt)] = (ix, rank, sym)

# identify the level with the most nodes
Cnt_Node = Counter((len(Pnt),Pnt[0]) for Pnt in Tree.keys())
Cnt_Lvl_L = sorted([(cnt,lvl) for (lvl,dx),cnt in Cnt_Node.items() if dx==-1])
cnt_max_l, lvl_max_l = Cnt_Lvl_L.pop()
assert Cnt_Lvl_L[-1][0] < cnt_max_l
Cnt_Lvl_R = sorted([(cnt,lvl) for (lvl,dx),cnt in Cnt_Node.items() if dx==1])
cnt_max_r, lvl_max_r = Cnt_Lvl_R.pop()
assert Cnt_Lvl_R[-1][0] < cnt_max_r

# extract the message
Node_Msg_L = \
sorted([(Pnt,sym) for Pnt,(ix,rank,sym) in Tree.items() if \
len(Pnt)==lvl_max_l and Pnt[0]==-1])
Node_Msg_R = \
sorted([(Pnt,sym) for Pnt,(ix,rank,sym) in Tree.items() if \
len(Pnt)==lvl_max_r and Pnt[0]==1])
ans = ''.join([sym for Pnt,sym in Node_Msg_L]) + \
''.join([sym for Pnt,sym in Node_Msg_R])
print(ans)

