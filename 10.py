fo = open("10.txt", "r")
# fo = open("small.txt", "r")

''' Parse '''
diagram = []
row_index = 0
start = (-1, -1)

for line in fo.readlines():
    diagram.append(line.strip())
    s_col = line.find("S")
    if s_col != -1:
        start = (row_index, s_col)
    row_index += 1

''' Part 1 '''
ans1 = 0


def check_for_valid_n(pos):
    ns = []
    py, px = pos[0], pos[1]
    for value in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        t = diagram[py + value[0]][px + value[1]]
        n_is_valid = False
        if t == '|' and value[0] != 0:
            n_is_valid = True
        elif t == '-' and value[1] != 0:
            n_is_valid = True
        elif t == 'L' and (value == (1, 0) or value == (0, -1)):
            n_is_valid = True
        elif t == 'J' and (value == (1, 0) or value == (0, 1)):
            n_is_valid = True
        elif t == '7' and (value == (-1, 0) or value == (0, 1)):
            n_is_valid = True
        elif t == 'F' and (value == (-1, 0) or value == (0, -1)):
            n_is_valid = True

        if n_is_valid:
            ns.append((py + value[0], px + value[1]))
    return ns


# initialise with stepping into one of the two valid n to start traversing border of the loop
ns = check_for_valid_n(start)
current = ns[0]
prev = start
step_count = 1
print(f'start={start} valid_ns={ns}, going into {current}')
# For part2 we need to know all positions that are part of the border
border_pos = set()
border_pos.add(start)

# Keep stepping into valid n that's not previous, continue until back to start
while current != start:
    t = diagram[current[0]][current[1]]
    next = []
    border_pos.add(current)
    if t == '|':
        next.append((current[0] + 1, current[1]))
        next.append((current[0] - 1, current[1]))
    elif t == '-':
        next.append((current[0], current[1] + 1))
        next.append((current[0], current[1] - 1))
    elif t == 'L':
        next.append((current[0] - 1, current[1]))
        next.append((current[0], current[1] + 1))
    elif t == 'J':
        next.append((current[0] - 1, current[1]))
        next.append((current[0], current[1] - 1))
    elif t == '7':
        next.append((current[0] + 1, current[1]))
        next.append((current[0], current[1] - 1))
    elif t == 'F':
        next.append((current[0] + 1, current[1]))
        next.append((current[0], current[1] + 1))

    # Select valid neighbour that isn't current location
    # print(f'step={step_count}, current={current}, next={next}')
    step_count += 1
    c_tmp = current
    if next[0] == prev:
        current = next[1]
    elif next[1] == prev:
        current = next[0]
    else:
        assert False
    prev = c_tmp

ans1 = step_count / 2

''' Part 2 '''
ans2 = 0


def get_true_identity_of_S(row_id, c_id):
    valid_ns = check_for_valid_n((row_id, c_id))
    above_n = (row_id - 1, c_id)
    below_n = (row_id + 1, c_id)
    left_n = (row_id, c_id - 1)
    right_n = (row_id, c_id + 1)
    if above_n in valid_ns and below_n in valid_ns:
        return '|'
    elif above_n in valid_ns and left_n in valid_ns:
        return 'J'
    elif above_n in valid_ns and right_n in valid_ns:
        return 'L'
    elif below_n in valid_ns and left_n in valid_ns:
        return '7'
    elif below_n in valid_ns and right_n in valid_ns:
        return 'F'
    else:
        # Still an ok mistery, not relevant
        return -1


# Scan diagram left to right, row by row, since single loop, each crossing of border implies 'inside loop'
# So with odd border crosses we are inside the loop, but need special handling when travelling along the border
border_crosses = 0
enclosed_tiles = 0
prev_corner = -1
for row_id in range(len(diagram)):
    row = diagram[row_id]
    for c_id in range(len(row)):
        c = row[c_id]
        # Handle border crossing but only if we actually are on the border
        if (row_id, c_id) in border_pos:
            # Decode what S actually is and update 'c' accordingly to act on it
            if c == 'S':
                c = get_true_identity_of_S(row_id, c_id)
            if c == '|':
                border_crosses += 1
                # Should never be on border between corners then
                assert prev_corner == -1
            # Starting a border (since traversing left to right)
            elif c in ['F', 'L']:
                prev_corner = c
            # Ending border, possibly crossing it with a correct "corner combination"
            elif c in ['7', 'J']:
                if (prev_corner == 'F' and c == 'J') or (prev_corner == 'L' and c == '7'):
                    border_crosses += 1
                prev_corner = -1
        # Count enclosed tile if fully inside border, independent on c due to possible junk
        elif border_crosses % 2 == 1:
            enclosed_tiles += 1
    # print(f'encloused: {enclosed_tiles}, at row_id {row_id}, row={row}')

ans2 = enclosed_tiles

# 6800 for part1
print(f'Answer part 1: {ans1}')
# 483 for part2
print(f'Answer part 2: {ans2}')
