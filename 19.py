
import re
import copy

fo = open("19.txt", "r")
#fo = open("small.txt", "r")


''' Parse '''
double_n_split = fo.read().split("\n\n")

inst = {}
for line in double_n_split[0].split("\n"):
    key_val_split = line.split("{")
    inst[key_val_split[0]] = key_val_split[1][:-1].split(",")
parts = []
for line in double_n_split[1].split("\n"):
    numbers = list(map(int, re.findall("[0-9]+", line)))
    d = {'x': numbers[0], 'm': numbers[1], 'a': numbers[2], 's': numbers[3]}
    parts.append(d)


''' Part 1 '''
ans1 = 0

def check_accepted(l, part):
    # "2,5 types", one R/A is return, 0,5 is direct no return, one conditional
    i = 0
    while i < len(l):
        if l[i] == 'R':
            return False
        elif l[i] == 'A':
            return True
        elif ":" not in l[i]:
            return check_accepted(inst[l[i]], part)
        else:
            con_key = l[i].split(":")
            if ">" in con_key[0]:
                pp_value = con_key[0].split(">")
                if part[pp_value[0]] > int(pp_value[1]):
                    if con_key[1] == 'R':
                        return False
                    elif con_key[1] == 'A':
                        return True
                    else:
                        return check_accepted(inst[con_key[1]], part)
            elif "<" in con_key[0]:
                pp_value = con_key[0].split("<")
                if part[pp_value[0]] < int(pp_value[1]):
                    if con_key[1] == 'R':
                        return False
                    elif con_key[1] == 'A':
                        return True
                    else:
                        return check_accepted(inst[con_key[1]], part)
            else:
                assert False
        i += 1

accepted = []
for p in parts:
    acc = check_accepted(inst["in"], p)
    if acc:
        accepted.append(p)

for a in accepted:
    for v in a.values():
        ans1 += v


''' Part 2 '''
ans2 = 0

# Start with all 4000**4 = 256000000000000
# then device them down the tree from 'in' into all leafs
# due to strict comparisons, no possible splits in a path, can keep xMin-xMax, mMin-mMax etc
start = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}

# End leaf adds itself (aka split borders) to R or A list
REJECTED = []
ACCEPTED = []

def traverse(l, borders):
    # split at each list instruction
    for op in l:
        if op == 'R':
            REJECTED.append(borders)     # Direct, so always last
        elif op == 'A':
            ACCEPTED.append(borders)     # Direct, so always last
        elif ":" not in op:
            traverse(inst[op], borders)  # Direct, so always last
        else:
            con_key = op.split(":")
            borders_split = copy.deepcopy(borders)
            if ">" in con_key[0]:
                skey_value = con_key[0].split(">")
                # Continues the loop, updated specified border
                borders[skey_value[0]][1] = int(skey_value[1])
                borders_split[skey_value[0]][0] = int(skey_value[1]) + 1
            elif "<" in con_key[0]:
                skey_value = con_key[0].split("<")
                # Continues the loop, updated specified border
                borders[skey_value[0]][0] = int(skey_value[1])
                borders_split[skey_value[0]][1] = int(skey_value[1]) - 1
            # Handle split part, True to condition
            if con_key[1] == 'R':
                REJECTED.append(borders_split)
            elif con_key[1] == 'A':
                ACCEPTED.append(borders_split)
            else:
                traverse(inst[con_key[1]], borders_split)

traverse(inst["in"], start)
# Count all combos in each ACCEPTED
for a in ACCEPTED:
    tmp = 1
    for v in a.values():
        inclusive_delta = v[1] - v[0] + 1
        tmp *= inclusive_delta
    ans2 += tmp


# 263678 for part1
print(f'Answer part 1: {ans1}')
# 125455345557345 for part2
print(f'Answer part 2: {ans2}')
