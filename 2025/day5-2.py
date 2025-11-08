import sys

def make_bone(Nums):
    Bone = []
    for f_num in Nums:
        place = False
        for row in Bone:
            if f_num < row[1] and row[0] == -1:
                row[0] = f_num
                place = True
                break
            elif f_num > row[1] and row[2] == -1:
                row[2] = f_num
                place = True
                break
        if not place:
            Bone.append( [-1, f_num, -1] )
    return Bone

# parsing
X = [l.strip() for l in open(sys.argv[1], 'r')]
S = {}
for x in X:
    f_id, f_num = x.split(':')
    S[int(f_id)] = tuple(map(int,f_num.split(',')))

# construct the fishbones
Bones = {}
Qual = {}
for f_id in S.keys():
    Bones[f_id] = make_bone(S[f_id])
    Qual[f_id] = int(''.join(str(row[1]) for row in Bones[f_id]))

# get the quality range
ans = max(Qual.values()) - min(Qual.values())
print(ans)

