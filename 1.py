
fo = open("1.txt", "r")
#fo = open("small.txt", "r")

integers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
           'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
sum1 = 0
sum2 = 0

for line in fo.readlines():
    first, posf = None, 9999
    last, posl = None, -1
    #print(line)
    # Try out all integer candidates
    for integer in integers:
        pos = line.find(integer)
        if pos != -1:
            # match, but is it better than existing
            if pos < posf:
                first = integer
                posf = pos
        # could have duplicates, so search from correct end
        pos = line.rfind(integer)
        if pos > posl:
            last = integer
            posl = pos
    sum1 += int(first+last)

    # Try out all text candidates
    for key, value in letters.items():
        pos = line.find(key)
        if pos != -1:
            if pos < posf:
                first = value
                posf = pos
        pos = line.rfind(key)
        if pos > posl:
            last = value
            posl = pos
    sum2 += int(first+last)
    #print(f'first+last={first+last} sum1={sum1}')

#54304 for part1
print(f'Answer part 1: {sum1}')
#54418 for part2
print(f'Answer part 2: {sum2}')
