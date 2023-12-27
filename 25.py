
#fo = open("25.txt", "r")
fo = open("small.txt", "r")


''' Parse '''
components = set()
nm_n = {}

for line in fo.readlines():
    s = line.strip().split(":")
    raw = [s[0]] + s[1].split()
    if s[0] in nm_n:
        nm_n[s[0]] += len(raw) - 1
    else:
        nm_n[s[0]] = len(raw) - 1
    for c in raw[1:]:
        components.add(c)
        if c in nm_n:
            nm_n[c] += 1
        else:
            nm_n[c] = 1

# hfx/pzl, bvb/cmg, and nvd/jqt
print(components)
print(nm_n)

# Check number of edges
nm_edges = 0
for edges in nm_n.values():
    nm_edges += edges
print(nm_edges)
# 6848 on real input, so 6848*6847*6846 = 320_997_000_576 possible combinations, to many


''' Part 1 '''
ans1 = 0

ans1 = len(components)


''' Part 2 '''
ans2 = 0


#  for part1
print(f'Answer part 1: {ans1}')
#  for part2
print(f'Answer part 2: {ans2}')
