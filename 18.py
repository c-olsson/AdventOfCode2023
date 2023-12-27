
import sys
import time

# High recursion during flood fill (without memoization)
sys.setrecursionlimit(50000)

#fo = open("18.txt", "r")
fo = open("small.txt", "r")


''' Parse '''
dig_plan = []
lagoon = set()  # First entrance sets origo
current = (0, 0)
lagoon.add(current)
min_x, max_x, min_y, max_y = 0, 0, 0, 0

for line in fo.readlines():
    split = line.strip().split()
    dig_plan.append(split)
    size = int(split[1])
    dir = split[0]
    dx, dy = 0, 0
    if dir == 'R':
        for dx in range(1, (1*size + 1)):
            lagoon.add((current[0] + dx, current[1]))
    elif dir == 'L':
        for dx in range(1, (1*size + 1)):
            lagoon.add((current[0] - dx, current[1]))
        dx = -dx
    elif dir == 'D':
        for dy in range(1, (1*size + 1)):
            lagoon.add((current[0], current[1] + dy))
    elif dir == 'U':
        for dy in range(1, (1*size + 1)):
            lagoon.add((current[0], current[1] - dy))
        dy = -dy
    current = (current[0] + dx, current[1] + dy)
    min_x = min(min_x, current[0])
    min_y = min(min_y, current[1])
    max_x = max(max_x, current[0])
    max_y = max(max_y, current[1])

def print_lagoon():
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in lagoon:
                if (x, y) == (0, 0):
                    print('S', end="")
                else:
                    print('#', end="")
            else:
                print('.', end="")
        print()

''' Part 1 '''
ans1 = 0

# Looking at the lagoon, there are no crossings like previous day, flood fill should do the trick
depth_counter = 0
def ff(c):
    global depth_counter
    depth_counter += 1
    if c in lagoon:
        return
    else:
        lagoon.add(c)
        #if depth_counter % 1000 == 0:
        #    print(f'Depth counter={depth_counter}')
        #    print_lagoon()
        #    time.sleep(1)
        for n in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ff((c[0] + n[0], c[1] + n[1]))

# Initialize flood with a point inside lagoon
print_lagoon()
ff((1, 1))
print()
print_lagoon()

ans1 = len(lagoon)

''' Part 2 '''
ans2 = 0


# 48503 for part1
print(f'Answer part 1: {ans1}')
#  for part2... 62 207 436 749 1146 1627 is scaled up (1,2,3,4,5,6) example and its area
print(f'Answer part 2: {ans2}')
