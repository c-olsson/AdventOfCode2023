
fo = open("4.txt", "r")
#fo = open("small.txt", "r")

''' Parse '''
cards = {}  # Save a dict of cards containing a list with a list of winning numbers and one for the elfs
copies_2 = {} # For part 2, keep track on each card_id's number of copies
for line in fo.readlines():
    card_split = line.strip().split(':')
    card_id = int(card_split[0].split()[1])
    cards[card_id] = []
    copies_2[card_id] = 1

    sub_split = card_split[1].split('|')
    cards[card_id].append(sub_split[0].split())
    cards[card_id].append(sub_split[1].split())
#print(cards)

''' Part 1 '''
sum1 = 0
for key, value in cards.items():
    points = 0
    for number in value[0]:
        if number in value[1]:
            if points == 0:
                points = 1
            else:
                points = points * 2
    sum1 += points

''' Part 2 '''
for key, value in cards.items():
    # Given that we won't get copies outside original set, add upp one for each correct copy as well the copies themself
    matches = 0
    for number in value[0]:
        if number in value[1]:
            matches += 1
    for inception in range(copies_2[key]):
        for m in range(matches):
            copies_2[key + 1 + m] += 1
#print(copies_2)
sum2 = 0
for c in copies_2.values():
    sum2 += c

# 23441 for part1
print(f'Answer part 1: {sum1}')
# 5923918 for part2
print(f'Answer part 2: {sum2}')
