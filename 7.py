
fo = open("7.txt", "r")
#fo = open("small.txt", "r")

''' Misc '''
CARD_RANK = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9,
             '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
CARD_RANK2 = {'A': 14, 'K': 13, 'Q': 12, 'J': 0, 'T': 10, '9': 9,
              '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
TYPE = {1: "High card", 2: "Pair", 3: "Two pairs", 4: "Three of a kind",
        5: "Full house", 6: "Four of a kind", 7: "Five of a kind"}

class Hand:
    def __init__(self, h, b, is_part1 = True):
        self.hand = h
        self.bet = b
        self.part1 = is_part1
        if is_part1:
            self.type_rank = self.get_type_rank(list(h))
        else:
            self.type_rank = self.get_type_rank2(list(h))

    def get_type_rank(self, h: list):
        counts = {}
        for k in CARD_RANK.keys():
            counts[k] = h.count(k)
        # Five of a kind
        if 5 in counts.values(): return 7
        # Four of a kind
        if 4 in counts.values(): return 6
        # Full house
        if 3 in counts.values() and 2 in counts.values(): return 5
        # Three of a kind
        if 3 in counts.values(): return 4
        # Two pair
        pairs = []
        for k, v in counts.items():
            if v == 2: pairs.append(k)
        if len(pairs) == 2: return 3
        # One pair
        if 2 in counts.values(): return 2
        # High card
        return 1

    def get_type_rank2(self, h: list):
        counts = {}
        for k, v in CARD_RANK.items():
            counts[k] = h.count(k)

        pairs = []
        threes = []
        jokers = h.count('J')
        for k, v in counts.items():
            if v == 3: threes.append(k)
            if v == 2: pairs.append(k)

        # Five of a kind (7)
        if 5 in counts.values(): return 7
        # Four of a kind (6)
        if 4 in counts.values():
            if jokers != 0:
                return 7
            else:
                return 6
        # Full house (5)
        if len(threes) == 1 and len(pairs) == 1:
            if jokers != 0:
                return 7
            else:
                return 5
        # Three of a kind (4)
        if len(threes) == 1:
            if jokers == 2:
                return 7
            elif jokers == 3:
                return 6
            elif jokers == 1:
                return 6
            else:
                return 4
        # Two pair (3)
        if len(pairs) == 2:
            if jokers == 2:
                return 6
            elif jokers == 1:
                return 5
            else:
                return 3
        # One pair (2)
        if 2 in counts.values():
            if jokers != 0:
                return 4
            else:
                return 2
        # High card (1)
        if jokers == 1:
            return 2
        else:
            return 1

    def __lt__(self, other):
        if self.type_rank < other.type_rank:
            return True
        elif self.type_rank > other.type_rank:
            return False
        else:
            # Compare card by card
            for i in range(5):
                if self.part1:
                    self_card_rank = CARD_RANK[self.hand[i]]
                    other_card_rank = CARD_RANK[other.hand[i]]
                else:
                    self_card_rank = CARD_RANK2[self.hand[i]]
                    other_card_rank = CARD_RANK2[other.hand[i]]
                if self_card_rank < other_card_rank:
                    return True
                elif self_card_rank > other_card_rank:
                    return False
            # Should only get here if there is an identical hand
            assert False


''' Parse '''
hands = []  # list of Hand objects
hands2 = []

for line in fo.readlines():
    split = line.split()
    hand = Hand(split[0], int(split[1]), True)
    hands.append(hand)
    hand2 = Hand(split[0], int(split[1]), False)
    hands2.append(hand2)


''' Part 1 '''
hands.sort()
ans1 = 0
sort_rank = 1
for h in hands:
    ans1 += sort_rank * h.bet
    sort_rank += 1

''' Part 2 '''
hands2.sort()
ans2 = 0
sort_rank2 = 1
for h in hands2:
    #print(f'h.hand={h.hand} h.type_rank={h.type_rank} aka {TYPE[h.type_rank]}')
    ans2 += sort_rank2 * h.bet
    sort_rank2 += 1

# 253603890 for part1
print(f'Answer part 1: {ans1}')
# 253630098 for part2
print(f'Answer part 2: {ans2}')
