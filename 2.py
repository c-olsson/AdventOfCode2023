
fo = open("2.txt", "r")
#fo = open("small.txt", "r")

COLORS = ['red', 'green', 'blue']

''' Parse '''
games = {}  # Save a dict of games containing a list with a dict for each sub set game
for line in fo.readlines():
    game_split = line.strip().split(':')
    game_id = int(game_split[0].split()[1])
    games[game_id] = []

    game_sets = game_split[1].split(';')
    for game_set in game_sets:
        game_set_split = game_set.split(',')
        dset = {'red': 0, 'green': 0, 'blue': 0}
        for pair in game_set_split:
            pair_split = pair.strip().split()
            dset[pair_split[1]] = int(pair_split[0])
        games[game_id].append(dset)
#print(games)


''' Part 1 '''
limit_1 = {'red': 12, 'green': 13, 'blue': 14}
sum1 = 0
for game_id, game in games.items():
    add_id = True
    for sub_game in game:
        # check if any color reached the limit in this sub game
        for c in COLORS:
            if sub_game[c] > limit_1[c]:
                #print(f'fake id {game_id}')
                add_id = False
                break
        if not add_id:
            break
    if add_id:
        #print(f'good id {game_id}')
        sum1 += game_id

''' Part 2 '''
sum2 = 0
for game_id, game in games.items():
    # check highest value for each color in the sub game
    # assumes there is at least all colors occur in at least one of the sub games
    dmax = {'red': 0, 'green': 0, 'blue': 0}
    for sub_game in game:
        for c in COLORS:
            if sub_game[c] > dmax[c]:
                dmax[c] = sub_game[c]
    # calculate power for these highest values
    tmp_power = 1
    for c in COLORS:
        tmp_power = tmp_power * dmax[c]
    sum2 += tmp_power


#2716 for part1
print(f'Answer part 1: {sum1}')
#72227 for part2
print(f'Answer part 2: {sum2}')
