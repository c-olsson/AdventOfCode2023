
fo = open("9.txt", "r")
#fo = open("small.txt", "r")


''' Parse '''
history = []

for line in fo.readlines():
    history.append(list(map(int, line.strip().split())))


''' Part 1 '''
''' Part 2 '''
ans1 = 0
ans2 = 0

for h in history:
    list_deep = [h]
    # go deeper until all values are the same in the most recent added depth list
    while min(list_deep[-1]) != max(list_deep[-1]):
        to_add = []
        last_added = list_deep[-1]
        for i in range(len(last_added) - 1):
            diff = last_added[i+1] - last_added[i]
            to_add.append(diff)
        list_deep.append(to_add)
        # Sanity check that we are not too deep
        assert len(to_add) != 1
    # Extract next value from the last value for each depth, bottom up
    #print(list_deep)
    next_value = 0
    prev_value = 0
    for d in range(len(list_deep)-1, -1, -1):
        current_depth_last_value = list_deep[d][-1]
        next_value += current_depth_last_value
        #print(f'{current_depth_last_value} added to next_value={next_value}')
        current_depth_first_value = list_deep[d][0]
        prev_value = current_depth_first_value - prev_value
        #print(f'{current_depth_last_value} reduced to prev_value={prev_value}')
    ans1 += next_value
    ans2 += prev_value


# 1853145119 for part1
print(f'Answer part 1: {ans1}')
# 923 for part2
print(f'Answer part 2: {ans2}')
