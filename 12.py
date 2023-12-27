
import re

#fo = open("12.txt", "r")
fo = open("small.txt", "r")


''' Parse '''

patterns = []
combos = []
patterns_part2 = []
combos_part2 = []
for line in fo.readlines():
    s = line.strip().split()
    patterns.append(s[0])
    combos.append(list(map(int, s[1].split(","))))
    # Part 2
    patterns_part2.append(s[0]+'?'+s[0]+'?'+s[0]+'?'+s[0]+'?'+s[0])
    combos_part2.append(5 * list(map(int, s[1].split(","))))


''' Part 1 '''
ans1 = 0

def try_for_valid_outcomes(pat, com):
    q_indexes = []
    for i in range(len(pat)):
        if pat[i] == "?":
            q_indexes.append(i)
    nm_questions = len(q_indexes)
    nm_valids = 0
    for attempt in range(2**nm_questions):
        # bit-mask to decide '#' or '.' for each index in a tmp pattern to evaluate
        tmp_pattern = list(pat)
        for j in range(len(q_indexes)):
            if 2**j & attempt == 0:
                tmp_pattern[q_indexes[j]] = "."
            else:
                tmp_pattern[q_indexes[j]] = "#"
        outcome = re.findall("#+", "".join(tmp_pattern))
        valid = True
        # To be valid outcome they need to be same amount as the correct combo states, for all matched items
        if len(outcome) == len(com):
            for j in range(len(com)):
                if len(outcome[j]) != com[j]:
                    valid = False
                    break
        else:
            valid = False
        if valid:
            #print(f'{"".join(tmp_pattern)} was valid for c={com}')
            nm_valids += 1
    return nm_valids


for i in range(len(patterns)):
    p = patterns[i]
    c = combos[i]
    valid_outcomes = try_for_valid_outcomes(p, c)
    print(f'{i}: Adding {valid_outcomes} more valids, {p} and {c}')
    ans1 += valid_outcomes


''' Part 2 '''
ans2 = 0

''' Takes really forever even for one line with many ?s
for i in range(len(patterns_part2)):
    p = patterns_part2[i]
    c = combos_part2[i]
    valid_outcomes = try_for_valid_outcomes(p, c)
    print(f'{i}: Adding {valid_outcomes} more valids')
    ans2 += valid_outcomes
'''

# 7541 for part1
print(f'Answer part 1: {ans1}')
#  for part2
print(f'Answer part 2: {ans2}')
