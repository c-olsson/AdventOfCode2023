
fo = open("13.txt", "r")
#fo = open("small.txt", "r")


''' Parse '''
patterns_raw = fo.read().split("\n\n")
patterns = []
patterns_T = []

for pattern in patterns_raw:
    patterns.append(pattern.split("\n"))

# Extract a Transponent version for equal handling
for pattern in patterns:
    pattern_T = []
    for c in range(len(pattern[0])):
        c_to_T = ""
        for r in range(len(pattern)):
            c_to_T += pattern[r][c]
        pattern_T.append(c_to_T)
    patterns_T.append(pattern_T)


''' Part 1 '''
ans1 = 0

def count_mismatch(s1, s2):
    assert len(s1) == len(s2)
    mismatch = len(s1)
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            mismatch -= 1
    return mismatch

# Updated for part 2 with smudge_used, always true for part 1
def evaluate_reflection(pattern, start_row, smudge_used):
    min_loop_len = min(start_row, len(pattern) - start_row)
    for i in range(min_loop_len):
        row1 = pattern[start_row - 1 - i]
        row2 = pattern[start_row + i]
        mm = count_mismatch(row1, row2)
        if smudge_used and mm != 0:
            return False
        elif mm == 1:
            smudge_used = True
        elif mm > 1:
            return False
    # "won't necessarily continue", implies it never is it seems
    if smudge_used:
        return True
    else:
        return False

def find_row_candidate(P, type):
    for row_id in range(1, len(P)):
        mm = count_mismatch(P[row_id], P[row_id - 1])
        if mm == 0:
            found_match = evaluate_reflection(P, row_id, True)
            if found_match:
                #print(f'Found match at {row_id}, type={type}')
                if type == 'C':
                    return row_id
                else:
                    return row_id*100
    return 0

for p_id in range(len(patterns)):
    ans1 += find_row_candidate(patterns[p_id], 'R')
    ans1 += find_row_candidate(patterns_T[p_id], 'C')


''' Part 2 '''
ans2 = 0

def find_row_candidate_part2(P, type):
    for row_id in range(1, len(P)):
        mm = count_mismatch(P[row_id], P[row_id - 1])
        found_match = False
        if mm <= 1:
            found_match = evaluate_reflection(P, row_id, False)
        if found_match:
            print(f'Found match at {row_id}, type={type}')
            if type == 'C':
                return row_id
            else:
                return row_id*100
    return 0

for p_id in range(len(patterns)):
    ret = find_row_candidate_part2(patterns[p_id], 'R')
    if ret == 0:
        ans2 += find_row_candidate_part2(patterns_T[p_id], 'C')
    else:
        ans2 += ret

# 30487 for part1
print(f'Answer part 1: {ans1}')
# 31954 for part2
print(f'Answer part 2: {ans2}')
