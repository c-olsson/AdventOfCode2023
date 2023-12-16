
fo = open("15.txt", "r")
#fo = open("small.txt", "r")


''' Parse '''
seq = fo.readline().strip().split(",")

''' Part 1 '''
def extract_number(s):
    current_value = 0
    for c in s:
        current_value += ord(c)
        current_value *= 17
        tmp_full = int(current_value / 256)
        current_value -= tmp_full * 256
    return current_value

ans1 = 0
for s in seq:
    ans1 += extract_number(s)


''' Part 2 '''
boxes = {}
for s in seq:
    if '-' in s:
        label = s[:-1]
        box_id = extract_number(label)
        box = boxes.get(box_id)
        if box:
            label_index_to_remove = None
            for i in range(len(box)):
                if box[i][0] == label:
                    label_index_to_remove = i
            if label_index_to_remove is not None:
                del box[label_index_to_remove]
    elif '=' in s:
        label = s[:-2]
        lens = s[-1]
        box_id = extract_number(label)
        box = boxes.get(box_id)
        if box:
            label_found = False
            for i in range(len(box)):
                if box[i][0] == label:
                    boxes[box_id][i] = (label, lens)
                    label_found = True
            if not label_found:
                label_lens = (label, lens)
                box.append(label_lens)
        else:
            label_lens = (label, lens)
            boxes[box_id] = [label_lens]
    else:
        assert False

# Boxes populated with lenses, extract focusing power
ans2 = 0
for box_list in boxes.values():
    if box_list:
        box_id = extract_number(box_list[0][0]) + 1
        for i in range(len(box_list)):
            slot_id = i + 1
            focal_length = int(box_list[i][1])
            ans2 += box_id * slot_id * focal_length


# 497373 for part1
print(f'Answer part 1: {ans1}')
# 259356 for part2
print(f'Answer part 2: {ans2}')
