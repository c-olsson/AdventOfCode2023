import time

fo = open("21.txt", "r")
#fo = open("small.txt", "r")


''' Parse '''
area = []
START = (-1, -1)
row_id = 0
for line in fo.readlines():
    raw = line.strip()
    l = list(raw)
    s_pos = raw.find('S')
    if s_pos != -1:
        l[s_pos] = '.'
        START = (row_id, s_pos)
    area.append(l)
    row_id += 1

NUM_SIGNS_PER_INPUT = len(area) * len(area[0])

''' Part 1 '''
ans1 = 0

# Simulate traveling of splitted 'O's, keep track of each steps in a set and forget old steps
steppers = set()
steppers.add(START)

def print_area():
    #print()
    dot_count = 0
    for row in range(len(area)):
        #print()
        for col in range(len(area[0])):
            if (row, col) in steppers:
                #print('O', end="")
                pass
            else:
                #print(area[row][col], end="")
                if (area[row][col]) == '.':
                    dot_count += 1
    #print()
    #time.sleep(0.1)
    return dot_count

# 6 steps small input
print_area()
for i in range(144):
    new_gen_steppers = set()
    for s in steppers:
        for d_step in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            sn = (s[0] + d_step[0], s[1] + d_step[1])
            if 0 <= s[0] + d_step[0] < len(area[0]) and 0 <= s[1] + d_step[1] < len(area):
                if area[sn[0]][sn[1]] == '.':
                    new_gen_steppers.add(sn)
    steppers = new_gen_steppers
    dc = print_area()
    print(f'Size steppers: {len(steppers)}, dc: {dc} of {NUM_SIGNS_PER_INPUT}')


ans1 = len(steppers)

''' Part 2 '''
ans2 = 0

# Trying various boarder handle for one board:
#   ignore outside boarder, toggle between 7675 and 7712
#   ignore one before boarder, toggle between 7415 and 7452
# hm, how many are left empty... about 44%, so quite alot, toggling with neighbours
#
# 26501365 / 64 = 414083.828125
# 26501365 % 64 = 53
# hm, so we roughly will spread out 414083 repeated frames in each direction
# answer should be somewhere around
#   (2 * 414083)**2 * 7675 = 5_263_967_238_292_300
# ... ish,  5263967238292300 is to high
# ...        526396723829230 is to low
# ...       2600000000000000 is to many quesses :P
# the diamond structure, so less populated in the diagonal directions

# 3809 for part1, 64 steps
print(f'Answer part 1: {ans1}')
#  for part2, 26501365 steps with repeating infinite boarders
print(f'Answer part 2: {ans2}')
