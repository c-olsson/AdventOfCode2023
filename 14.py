
fo = open("14.txt", "r")
#fo = open("small.txt", "r")


''' Parse '''
area = []

for line in fo.readlines():
    area.append(list(line.strip()))

def print_area():
    for r in area:
        print(r)

''' Part 1 '''
ans1 = 0

def tilt_north():
    for c in range(len(area[0])):
        ok_row = -1
        for r in range(len(area)):
            t = area[r][c]
            if t == '.' and ok_row == -1:
                ok_row = r
            elif t == '#':
                ok_row = -1
            elif t == 'O' and ok_row != -1:
                area[ok_row][c] = 'O'
                area[r][c] = '.'
                ok_row += 1
            else:
                # ignore '.' if already have valid cell to populate
                # ignore '0' if there is no valid cell to move to
                pass

#print_area()
print("\n")
print_area()

# Count load on support beam
load = len(area)
for row in area:
    nm_0 = row.count('O')
    ans1 += nm_0 * load
    load -= 1


''' Part 2 '''
ans2 = 0

# Part 1 approach to slow (on bigger input) to iterate all cells 4 billion times + load calculation, e.g
# for cycle in range(1000000000):
#     tilt_north()

# 110779 for part1
print(f'Answer part 1: {ans1}')
#  for part2
print(f'Answer part 2: {ans2}')
