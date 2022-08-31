# Score categories.
# Change the values as you see fit.
from collections import Counter

YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    total = 0

    if category == YACHT:
        total += 50 if len(set(dice)) == 1 else 0
    elif category in {ONES, TWOS, THREES, FOURS, FIVES, SIXES}:
        total += category * sum(throw == category for throw in dice)
    elif category == FULL_HOUSE:
        total += sum(dice) if set(Counter(dice).values()) == {2, 3} else 0
    elif category == FOUR_OF_A_KIND:
        side, times = Counter(dice).most_common(1)[0]
        total += 4* side if times in [4, 5] else 0
    elif category == LITTLE_STRAIGHT:
        total += 30 if set(dice)  == {1, 2, 3, 4, 5} else 0
    elif category == BIG_STRAIGHT:
        total =+ 30 if set(dice) == {2, 3, 4, 5, 6} else 0
    elif category == CHOICE:
        total += sum(dice)
    else:
        raise ValueError(f'unknown category: {category}')
    return total