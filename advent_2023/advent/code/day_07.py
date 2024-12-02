from advent_2023.advent.utilities import get_digit_from_string

card_order = {
    'A': 1, 'K': 2, 'Q': 3, 'J': 4, 'T': 5, '9': 6, '8': 7, '7': 8, '6': 9, '5': 10, '4': 11, '3': 12, '2': 13
}

hand_rank = {
    'fives': 1, 'fours': 2, 'full_house': 3, 'threes': 4, 'two_pair': 5, 'one_pair': 6, 'high_card': 7
}


def part_one(data):
    hands = parse(data)
    for hand in hands:
        pass

def get_hand_rank(hand):
    if len(set(hand)) == 1:
        return 'fives'


def parse(data):
    hands = dict()
    for hand in data.split('\n'):
        print(hand)
        print(hand.split(' '))
        cards, bet = hand.split(' ')
        hands[cards] = {'bet': get_digit_from_string(bet)[0]}
    return hands


inputs = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

if __name__ == '__main__':
    # with open('../inputs/day_06.txt', 'r') as f:
    #     inputs = f.read().split('\n')

    print(part_one(inputs))
    # print(part_two(data))  # 35,961,505