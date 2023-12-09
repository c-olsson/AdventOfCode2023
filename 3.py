
fo = open("3.txt", "r")
#fo = open("small.txt", "r")

INTEGERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
GEAR = '*'
INVALID_GEAR_COORD = (-1, -1)

''' Parse '''
engine = []  # Use a matrix in form of a list of string rows
# Add a "dont care" border to avoid out of range checks, will be 1 indexed
for line in fo.readlines():
    engine.append('.' + line.strip() + '.')
MAX_C = len(engine[0])
# Top and bottom "dont care" border
engine = [MAX_C*'.'] + engine
engine.append(MAX_C*'.')
MAX_R = len(engine)

''' Util '''
DX = [-1,  0,  1, -1, 1, -1, 0, 1]
DY = [-1, -1, -1,  0, 0,  1, 1, 1]
def evaluate_n_symbols(row :int, col :int):
    a_neighbour_is_a_symbol = False
    n_gear_coordinate = INVALID_GEAR_COORD
    for i in range(len(DX)):
        n_char = engine[row+DY[i]][col+DX[i]]
        if n_char not in INTEGERS and n_char != '.':
            a_neighbour_is_a_symbol = True
            if n_char == GEAR:
                n_gear_coordinate = (row+DY[i], col+DX[i])
    return a_neighbour_is_a_symbol, n_gear_coordinate


''' Part 1 '''
''' Part 2 '''
ans1 = 0
ans2 = 0
# Need to save part numbers for gears
gear_numbers = {}

for ri in range(1, MAX_R):
    tmp_num = ''
    tmp_valid = False
    tmp_n_gear_coord = INVALID_GEAR_COORD
    for ci in range(1, MAX_C):
        c = engine[ri][ci]
        # Accumulate number as a string and continuously check for adjacent symbol if not already found
        if c in INTEGERS:
            tmp_num += c
            c_had_n_symbol, n_gear_coord = evaluate_n_symbols(ri, ci)
            # Only update symbol and gear validity if we haven't found any yet
            if not tmp_valid and c_had_n_symbol:
                tmp_valid = True
            if tmp_n_gear_coord == INVALID_GEAR_COORD and n_gear_coord != INVALID_GEAR_COORD:
                # Will only register for one gear, assumes one number is not related to two gears (input looks ok)
                tmp_n_gear_coord = n_gear_coord
        else:
            # Evaluate the number, dot or symbol have same affect
            if tmp_num != '' and tmp_valid:
                ans1 += int(tmp_num)
                if len(tmp_num) == 4:
                    pass
                # Part 2, add number to gear dict for later evaluation
                if tmp_n_gear_coord != INVALID_GEAR_COORD:
                    try:
                        gear_numbers[tmp_n_gear_coord].append(int(tmp_num))
                    except KeyError:
                        gear_numbers[tmp_n_gear_coord] = []
                        gear_numbers[tmp_n_gear_coord].append(int(tmp_num))
            # Reset accumulator variables
            tmp_num = ''
            tmp_valid = False
            tmp_n_gear_coord = INVALID_GEAR_COORD

# Check all numbers adjacent to a '*' and add upp gear ratio if it is exactly 2 of them
for gear_numbers in gear_numbers.values():
    if len(gear_numbers) == 2:
        gear_ratio = gear_numbers[0] * gear_numbers[1]
        ans2 += gear_ratio


# 533775 for part1
print(f'Answer part 1: {ans1}')
# 78236071 for part2
print(f'Answer part 2: {ans2}')
