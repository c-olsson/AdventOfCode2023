
import re

#fo = open("24.txt", "r")
fo = open("small.txt", "r")


''' Parse '''
starts = []
speeds = []

for line in fo.readlines():
    values = re.findall("-?\d+", line)
    starts.append([int(x) for x in values[:3]])
    speeds.append([int(x) for x in values[3:]])


''' Part 1 '''
ans1 = 0

# linear equations: y=kx+m, k=dy/dx, m=x1-k*y1, note that paralellel if k1*k2=-1
# addition method can then solve intersection of two equations

intersections = []
for i in range(len(starts)):
    for j in range(len(starts)):
        if j > i:
            k1 = speeds[i][1] / speeds[i][0]
            k2 = speeds[j][1] / speeds[j][0]
            m1 = starts[i][1] - k1*starts[i][0]
            m2 = starts[j][1] - k2*starts[j][0]
            if k1 == k2:
                continue
            # not parallel, find crossing point by canceling y part with -1
            xpart = k2 - k1
            mpart = m1 - m2
            x = mpart / xpart
            y = k1*x + m1
            intersections.append((x, y, i, j))

print(f'num intersections: {len(intersections)}')

def is_future_crossing(dx, dy, x_speed, y_speed):
    if dx < 0 and x_speed < 0 or 0 < dx and x_speed > 0:
        if dy < 0 and y_speed < 0 or 0 < dy and y_speed > 0:
            return True
    return False

for intersect in intersections:
    # Inside test area
    #if 7 <= intersect[0] <= 27 and 7 <= intersect[1] <= 27:
    if 200000000000000 <= intersect[0] <= 400000000000000 and 200000000000000 <= intersect[1] <= 400000000000000:
        # Crossing is about to happen in the future, difference start-crossing has same sign as vel for both equations
        index1 = intersect[2]
        x1_to_be_crossed = is_future_crossing(intersect[0] - starts[index1][0],
                                              intersect[1] - starts[index1][1],
                                              speeds[index1][0],
                                              speeds[index1][1])
        index2 = intersect[3]
        x2_to_be_crossed = is_future_crossing(intersect[0] - starts[index2][0],
                                              intersect[1] - starts[index2][1],
                                              speeds[index2][0],
                                              speeds[index2][1])
        if x1_to_be_crossed and x2_to_be_crossed:
            ans1 += 1

''' Part 2 '''
ans2 = 0

# part2, add z intersection
# ... need 3 3d lines to extract a new 3d line that would intersect all those 3



# 15558 for part1
print(f'Answer part 1: {ans1}')
#  for part2
print(f'Answer part 2: {ans2}')
