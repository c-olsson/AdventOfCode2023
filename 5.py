
fo = open("5.txt", "r")
#fo = open("small.txt", "r")

INTS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

''' Parse '''
# Save seeds and step through map instructions for each
seeds = list(map(int, fo.readline().strip().split(':')[1].split()))
maps = {}  # Save map instructions, keyed by its order, valued by a list of lists
map_key = 0

for line in fo.readlines():
    if not line.strip():
        map_key += 1
        maps[map_key] = []
        continue
    if line[0] not in INTS:
        continue
    # Only number lines now
    numbers = list(map(int, line.strip().split()))
    maps[map_key].append(numbers)

''' Part 1 '''
ans1 = 0
seeds_mapped = []
for s in seeds:
    s_mapped = s
    #print(f'Handling seed {s_mapped}')
    for mult_list in maps.values():
        for l in mult_list:
            range_min = l[1]
            range_max = range_min + l[2]
            if range_min <= s_mapped < range_max:
                new = s_mapped + l[0]-l[1]
                #print(f'mapping {s_mapped} to {new}')
                s_mapped = new
                break
    seeds_mapped.append(s_mapped)

ans1 = min(seeds_mapped)

''' Part 2 '''
sum2 = 0
# Hm, big numbers, go with an approach to remember ranges for each depth step
# Doable since we are only interested in the lowest location from any seed, no need for backtracking

# Initialize index=0 with the seed ranges, (Xmin, Xmax) tuple for each interval
ranges = {0: []}
for i in range(0, len(seeds), 2):
    r = (seeds[i], seeds[i] + seeds[i+1] - 1)
    ranges[0].append(r)

def add_new_ranges(r, m, depth):
    # add only overlapping ranges, there are six different combinations of range overlap
    # return
    #   anything_was_mapped: a map function was utilized
    #   list_of_leftovers:   none, one range or two ranges that had "overhang" for this map function ranges
    mmin, mmax = m[1], m[1] + m[2] - 1
    rmin, rmax = r[0], r[1]
    conversion = m[0] - m[1]
    # No overlap (x2)
    if rmin > mmax or rmax < mmin:
        return False, []
    # Full inclosure/handle of map function
    if rmin >= mmin and rmax <= mmax:
        ranges[depth].append((rmin + conversion, rmax + conversion))
        return True, []
    # Left as well Right "overhang"
    if rmin < mmin and rmax > mmax:
        ranges[depth].append((mmin + conversion, mmax + conversion))
        return True, [(rmin, mmin - 1), (mmax + 1, rmax)]
    # Left "overhang"
    if rmin < mmin and rmax <= mmax:
        ranges[depth].append((mmin + conversion, rmax + conversion))
        return True, [(rmin, mmin - 1)]
    # Right "overhang"
    if rmin >= mmin and rmax > mmax:
        ranges[depth].append((rmin + conversion, mmax + conversion))
        return True, [(mmax + 1, rmax)]


for depth in range(1, len(maps) + 1, 1):
    ranges[depth] = []
    # For previous depth, handle mapping of each range by applying it to these depth map functions
    for r in ranges[depth - 1]:
        anything_mapped = False
        for m in maps[depth]:
            mapped, left_over = add_new_ranges(r, m, depth)
            if not anything_mapped and mapped:
                anything_mapped = True
            # To handle partial range handle, append the part not handled to be processed separately later.
            # Skip any remaining mapping, eventually each split range should be fully mapped, map function or not.
            if mapped and left_over:
                for lo in left_over:
                    ranges[depth - 1].append(lo)
                break
        # No mapping found for this range in this depth, add its full range for next depth level
        if not anything_mapped:
            ranges[depth].append(r)

print(f'All final ({len(ranges[len(maps)])}) location ranges={ranges[len(maps)]}')
# Extract the lowest rmin in the deepest level, aka locations
current_min = 10**12
for r in ranges[len(maps)]:
    if r[0] < current_min:
        current_min = r[0]

ans2 = current_min

# 484023871 for part1
print(f'Answer part 1: {ans1}')
# 46294175 for part2
print(f'Answer part 2: {ans2}')
