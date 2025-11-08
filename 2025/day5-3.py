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

def is_greater(Bone0, f_id0, Bone1, f_id1):
    # compare the qualities of the bones
    qual0 = int(''.join(str(row[1]) for row in Bone0))
    qual1 = int(''.join(str(row[1]) for row in Bone1))
    if qual0 > qual1:
        return True
    elif qual0 < qual1:
        return False
    # compare the bone numbers by level
    nrow = min(len(Bone0), len(Bone1))
    for i in range(nrow):
        num0 = int(''.join(str(num) for num in Bone0[i] if num != -1))
        num1 = int(''.join(str(num) for num in Bone1[i] if num != -1))
        if num0 > num1:
            return True
        elif num0 < num1:
            return False
    # compare the ids
    if f_id0 > f_id1:
        return True
    elif f_id0 < f_id1:
        return False
    assert False

# parsing
X = [l.strip() for l in open(sys.argv[1], 'r')]
S = {}
for x in X:
    f_id, f_num = x.split(':')
    S[int(f_id)] = tuple(map(int,f_num.split(',')))

# construct the fishbones
Bones = {}
for f_id in S.keys():
    Bones[f_id] = make_bone(S[f_id])

# sort the swords
Sort = []
for f_id0, Bone0 in Bones.items():
    for i, f_id1 in enumerate(Sort):
        Bone1 = Bones[f_id1]
        if is_greater(Bone0, f_id0, Bone1, f_id1):
            Sort = Sort[:i] + [f_id0] + Sort[i:]
            break
    if f_id0 not in Sort:
        Sort.append(f_id0)

# calculate the checksum
ans = sum((i+1) * f_id for i,f_id in enumerate(Sort))
print(ans)

