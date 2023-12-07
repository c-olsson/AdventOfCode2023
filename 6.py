
import math

fo = open("6.txt", "r")
#fo = open("small.txt", "r")

''' Parse '''
# Save max time allowed and distance in separate lists and step through map instructions for each
tmax_str = fo.readline().strip().split(':')[1].split()
tmax = list(map(int, tmax_str))
dmax_str = fo.readline().strip().split(':')[1].split()
dmax = list(map(int, dmax_str))


''' Part 1 '''
ans1 = 1
# Distance = Tpress * (Tmax - Tpress), aka 2nd order equation that is symmetric
# Optimal distance is then Tpress = Tmax/2, giving Dmax = Tmax2 / 4
# Need to evaluate what Tpress integers gives higher than previous Drecord
# We can utilize the symmetric to step backwards from optimal

def distance(t, tmax):
    return t * (tmax - t)

for i in range(len(tmax)):
    t = math.floor(tmax[i] / 2)
    optimal_start = False
    if t == (tmax[i] / 2):
        # aka even
        optimal_start = True
        #print(f'optimal start d={distance(t, tmax[i])}')
    count = 0
    while distance(t, tmax[i]) > dmax[i]:
        #print(f'c={count} t={t} d={distance(t, tmax[i])}')
        count += 1
        t -= 1
    count = count * 2
    # remove one if we actually started at the optimal, no symmetry use then
    if optimal_start:
        count -= 1
    #print(count)
    ans1 = ans1 * count

''' Part 2  '''
ans2 = 1
# More optimal solution would be to calculate the time for when previous record is and take diff to Toptimal
tmax = int(''.join(tmax_str))
dmax = int(''.join(dmax_str))

# lazy reuse of part 1 but with single values instead of lists
t = math.floor(tmax / 2)
optimal_start = False
#print(f'part 2 dmax={dmax} tmax={tmax}')
if t == (tmax / 2):
    # aka even
    optimal_start = True
    #print(f'optimal start d={distance(t, tmax)}')
count = 0
while distance(t, tmax) > dmax:
    #print(f'c={count} t={t} d={distance(t, tmax[i])}')
    count += 1
    t -= 1
count = count * 2
# remove one if we actually started at the optimal, no symmetry use then
if optimal_start:
    count -= 1
ans2 = count

# 2344708 for part1
print(f'Answer part 1: {ans1}')
# 30125202 to low for part2
print(f'Answer part 2: {ans2}')
