
fo = open("11.txt", "r")
#fo = open("small.txt", "r")


''' Parse '''
cosmos = []
galaxies = {}
no_g_rows = []
row_index = 0
galaxy_id = 1  # Hm, they 1 indexed the galaxies in example
for line in fo.readlines():
    cosmos.append(line.strip())
    galaxy_found = False
    for ci in range(len(line)):
        if line[ci] == '#':
            galaxy_found = True
            galaxies[galaxy_id] = (row_index, ci)
            galaxy_id += 1
    if not galaxy_found:
        no_g_rows.append(row_index)
    row_index += 1

# We parsed all rows now, check for columns without any galaxy
no_g_col = []
for col_index in range(len(cosmos[0])):
    galaxy_found = False
    for row in cosmos:
        if row[col_index] == '#':
            galaxy_found = True
            break
    if not galaxy_found:
        no_g_col.append(col_index)


''' Part 1 '''
''' Part 2 '''
ans1 = 0
ans2 = 0
dist_counted = 0
for k1, g1 in galaxies.items():
    for k2, g2 in galaxies.items():
        # Evaluate Manahattan distance (+empty row/col space), so galax_id only "infront"
        if k1 < k2:
            dist = abs(g2[0] - g1[0])
            dist += abs(g2[1] - g1[1])
            # Part 1: Add 1 for each empty row/col passed, by definition cant be inclusive range due to a galaxy there
            extra_rows = 0
            for r in no_g_rows:
                if g1[0] < r < g2[0] or g2[0] < r < g1[0]:
                    extra_rows += 1
            extra_cols = 0
            for c in no_g_col:
                if g1[1] < c < g2[1] or g2[1] < c < g1[1]:
                    extra_cols += 1
            dist1 = dist + extra_rows + extra_cols
            # Part 2: Add 10**6 instead of +1 as in part 1, minus one is for one empty step already part of input
            dist2 = dist + (10**6 - 1) * (extra_rows + extra_cols)
            dist_counted += 1
            ans1 += dist1
            ans2 += dist2
            #print(f'{k1}->{k2} is {dist1}/{dist2}, {dist_counted} counted')


# 9599070 for part1
print(f'Answer part 1: {ans1}')
# 842645913794 for part2
print(f'Answer part 2: {ans2}')
