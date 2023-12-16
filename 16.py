import time

fo = open("16.txt", "r")
#fo = open("small.txt", "r")


''' Parse '''
area = []

for line in fo.readlines():
    area.append(line.strip())

''' Part 1 '''
ans1 = 0

class Ray():
    def __init__(self, start_x: int, start_y: int, step_x: int, step_y: int):
        self.x = start_x
        self.y = start_y
        self.dx = step_x
        self.dy = step_y
        self.inside = True

# Create list of rays to move each stepping
rays = [Ray(0, 0, 1, 0)]
# Create a separate Set with unique coordinates for visited places, wanted to maximize
energized = set()
# Explosion of ray objects if no visited with direction check, multiple small loops I suppose
visited_with_direction = set()

def move_rays():
    for ray in rays:
        if not ray.inside:
            continue
        # Add energized and visited info
        energized.add((ray.x, ray.y))
        visited_with_direction.add((ray.x, ray.y, ray.dx, ray.dy))
        # Adjust directions according to current symbol
        current_symbol = area[ray.y][ray.x]
        if current_symbol == '.':
            pass
        elif current_symbol == '|':
            if ray.dy == 0:
                # Only split if it is in new valid location and with new direction
                s_ray = Ray(ray.x, ray.y - 1, 0, -1)
                if ray.y - 1 >= 0 and (s_ray.x, s_ray.y, s_ray.dx, s_ray.dy) not in visited_with_direction:
                    rays.append(s_ray)
                ray.dx = 0
                ray.dy = 1
        elif current_symbol == '-':
            if ray.dx == 0:
                # Only split if it is in new valid location and with new direction
                s_ray = Ray(ray.x - 1, ray.y, -1, 0)
                if ray.y - 1 >= 0 and (s_ray.x, s_ray.y, s_ray.dx, s_ray.dy) not in visited_with_direction:
                    rays.append(s_ray)
                ray.dx = 1
                ray.dy = 0
        elif current_symbol == '/':
            if ray.dx == 1:
                ray.dx = 0
                ray.dy = -1
            elif ray.dx == -1:
                ray.dx = 0
                ray.dy = 1
            elif ray.dy == 1:
                ray.dx = -1
                ray.dy = 0
            else:
                ray.dx = 1
                ray.dy = 0
        elif current_symbol == '\\':
            if ray.dx == 1:
                ray.dx = 0
                ray.dy = 1
            elif ray.dx == -1:
                ray.dx = 0
                ray.dy = -1
            elif ray.dy == 1:
                ray.dx = 1
                ray.dy = 0
            else:
                ray.dx = -1
                ray.dy = 0
        # Move according to adjusted directions
        ray.x += ray.dx
        ray.y += ray.dy
        # Check if it went outside border, mark it dead if so
        if ray.x < 0 or ray.x >= len(area[0]) or ray.y < 0 or ray.y >= len(area):
            ray.inside = False


def print_area():
    for y in range(len(area)):
        for x in range(len(area[0])):
            if (x,y) in energized:
                print('#', end='')
            else:
                print('.', end='')
        print()

def simulate_end_energy_level(start_x, start_y, step_x, step_y):
    # Re-initialize starting point and essential containers, update for part 2
    global rays, energized, visited_with_direction
    rays = [Ray(start_x, start_y, step_x, step_y)]
    energized = set()
    visited_with_direction = set()
    # Consider no growth (stable) when it kept same energize level for area size amount of steps
    SIZE = len(area)
    history = {0: -1, SIZE-1: 1}
    step = 0
    while min(history.values()) != max(history.values()):
        move_rays()
        step += 1
        history[step % SIZE] = len(energized)
        # Simulation is... very beautiful!!!
        #print(f'energized size={len(energized)}')
        #print_area()
        #time.sleep(0.1)
    return len(energized)

ans1 = simulate_end_energy_level(0, 0, 1, 0)

''' Part 2 '''
ans2 = 0

# Part 2 is to try all possible initiations to find maximum energize
max_energy = 0
# Try all coming from above and below
for x in range(len(area[0])):
    candidate = simulate_end_energy_level(x, 0, 0, 1)
    max_energy = max(max_energy, candidate)
    candidate = simulate_end_energy_level(x, len(area) - 1, 0, -1)
    max_energy = max(max_energy, candidate)
# Try all coming from left and right
for y in range(len(area)):
    candidate = simulate_end_energy_level(0, y, 1, 0)
    max_energy = max(max_energy, candidate)
    candidate = simulate_end_energy_level(len(area[0]) - 1, y, -1, 0)
    max_energy = max(max_energy, candidate)

# Max given with start conditions
# simulate_end_energy_level(36, len(area) - 1, 0, -1)
ans2 = max_energy

# 6978 for part1
print(f'Answer part 1: {ans1}')
# 7315 for part2
print(f'Answer part 2: {ans2}')
