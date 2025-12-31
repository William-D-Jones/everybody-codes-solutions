import sys
import re
from collections import Counter

# parsing
X = [line.strip() for line in open(sys.argv[1], 'r')]
Inst = []
for x in X:
    M_Add = re.match(\
    r'^ADD id=([0-9]+) left=\[([0-9]+),(.+)\] right=\[([0-9]+),(.+)\]$', x)
    M_Swap = re.match(r'^SWAP ([0-9]+)', x)
    if M_Add and not M_Swap:
        ix = int(M_Add.group(1))
        rank_l = int(M_Add.group(2))
        sym_l = M_Add.group(3)
        rank_r = int(M_Add.group(4))
        sym_r = M_Add.group(5)
        Inst.append( ('add',ix,rank_l,sym_l,rank_r,sym_r) )
    elif M_Swap and not M_Add:
        ix_swap = int(M_Swap.group(1))
        Inst.append( ('swap',ix_swap) )
    else:
        assert False

# construct the tree
Tree = {}
for inst in Inst:
    if inst[0]=='add':
        op, ix, rank_l, sym_l, rank_r, sym_r = inst
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
    elif inst[0]=='swap':
        op, ix_swap = inst
        Pnt_Swap = sorted([Pnt for Pnt, (ix, rank, sym) in \
        Tree.items() if ix==ix_swap])
        assert len(Pnt_Swap)==2
        # swap the ranks and symbols
        ix0, rank0, sym0 = Tree[Pnt_Swap[0]]
        ix1, rank1, sym1 = Tree[Pnt_Swap[1]]
        assert ix0==ix1
        Tree[Pnt_Swap[0]] = (ix0, rank1, sym1)
        Tree[Pnt_Swap[1]] = (ix1, rank0, sym0)
    else:
        assert False

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

