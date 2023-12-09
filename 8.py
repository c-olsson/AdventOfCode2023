
import re
import math

fo = open("8.txt", "r")
#fo = open("small.txt", "r")


''' Parse '''
inst = fo.readline().strip()
fo.readline()  # ignore
tree = {}  # Save binary tree as a dict of pairs
part2_starts = []

for line in fo.readlines():
    tripples = re.findall("[A-Z]{3}", line)
    tree[tripples[0]] = tripples[1:]
    part2 = re.findall("[A-Z]{2}A\s=", line)
    if part2:
        part2_starts.append(tripples[0])

''' Part 1 '''
steps = 0
index = 0
nex_to_visit = "AAA"

while nex_to_visit != "ZZZ":
    if inst[index] == 'L':
        nex_to_visit = tree[nex_to_visit][0]
    else:
        nex_to_visit = tree[nex_to_visit][1]
    steps += 1
    index = steps % len(inst)

ans1 = steps


''' Part 2 '''
steps = 0
index = 0
nex_to_visit = part2_starts
simultaneous_places = len(nex_to_visit)

# Loop until we register a periodicy for each path (part 1 approach would take days it seems)
tot_steps_at_periodic = {}
while len(tot_steps_at_periodic.keys()) < simultaneous_places:
    if inst[index] == 'L':
        for i in range(simultaneous_places):
            nex_to_visit[i] = tree[nex_to_visit[i]][0]
    else:
        for i in range(simultaneous_places):
            nex_to_visit[i] = tree[nex_to_visit[i]][1]
    steps += 1
    index = steps % len(inst)

    for key_index in range(len(nex_to_visit)):
        if nex_to_visit[key_index][2] == 'Z':
            try:
                tot_steps_at_periodic[key_index].append(steps)
            except KeyError:
                tot_steps_at_periodic[key_index] = []
                tot_steps_at_periodic[key_index].append(steps)

# The periodicy for each path is consistently reoccuring
# 0: [0, 13207, 26414, 39621, 52828, 66035, 79242]
# 1: [0, 19951, 39902, 59853, 79804]
# 2: [0, 14893, 29786, 44679, 59572, 74465]
# 3: [0, 12083, 24166, 36249, 48332, 60415, 72498, 84581]
# 4: [0, 20513, 41026, 61539, 82052]
# 5: [0, 22199, 44398, 66597, 88796]
# ... simulating stepping of each path takes forever.
# Fortunately math and primes gives us that the least common devider between them gives us the wanted answer

periodicy = [p_list[0] for p_list in tot_steps_at_periodic.values()]
print(f'Periodicy for all simultaneous tracks: {periodicy}')

def factorize(n):
    factors =[]
    for t in range(2, (math.ceil((n / 2) + 1))):
        if n % t == 0:
            factors.append(t)
    return factors

prime_factors = set()
for p in periodicy:
    factors = factorize(p)
    for f in factors:
        prime_factors.add(f)
print(f'Unique prime factors for all tracks {prime_factors}')
ans2 = 1
for f in prime_factors:
    ans2 *= f

# 13207 for part1
print(f'Answer part 1: {ans1}')
# 12324145107121 for part2
print(f'Answer part 2: {ans2}')
