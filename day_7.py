from dataclasses import dataclass
from collections import Counter

with open('inputs/day_7_input.txt') as f:
    inputs = f.read().splitlines()

with open('inputs/day_7_test.txt') as f:
    test = f.read().splitlines()


@dataclass
class Hand:
    card_1: int
    card_2: int
    card_3: int
    card_4: int
    card_5: int
    bet: int
    combination: int
    card_weights = {'A': 14, 'K': 13, 'Q': 12, 'J': 1,
                    'T': 10, '9': 9, '8': 8, '7': 7,
                    '6': 6, '5': 5, '4': 4, '3': 3,
                    '2': 2}

    def __init__(self, hand: str, bet: str):
        self.bet = int(bet)
        cards = list(hand)
        self.card_1 = self.card_weights.get(cards[0].upper(), 0)
        self.card_2 = self.card_weights.get(cards[1].upper(), 0)
        self.card_3 = self.card_weights.get(cards[2].upper(), 0)
        self.card_4 = self.card_weights.get(cards[3].upper(), 0)
        self.card_5 = self.card_weights.get(cards[4].upper(), 0)
        self.all_cards = [self.card_1, self.card_2, self.card_3, self.card_4, self.card_5]
        self.combination = self._determine_combination()

    def _determine_combination(self):
        card_counts = Counter(card for card in self.all_cards)
        count_frequencies = list(card_counts.values())
        count_frequencies.sort(reverse=True)
        joker_count = sum(card == 1 for card in self.all_cards)

        if count_frequencies[0] == 5:
            return 6  # Five of a kind
        elif count_frequencies[0] == 4:
            if joker_count == 1 or joker_count == 4:
                return 6
            return 5  # Four of a kind
        elif count_frequencies[0] == 3 and count_frequencies[1] == 2:
            if joker_count == 2 or joker_count == 3:
                return 6
            return 4  # Full house
        elif count_frequencies[0] == 3:
            if joker_count == 1 or joker_count == 3:
                return 5
            return 3  # Three of a kind
        elif count_frequencies[0] == 2 and count_frequencies[1] == 2:
            if joker_count == 1:
                return 4
            if joker_count == 2:
                return 5
            return 2  # Two pairs
        elif count_frequencies[0] == 2:
            if joker_count == 1 or joker_count == 2:
                return 3
            return 1  # One pair
        else:
            if joker_count == 1:
                return 1
            return 0  # High card

    def __lt__(self, other):
        if self.combination < other.combination:
            return True
        elif self.combination == other.combination:
            for card_self, card_other in zip(self.all_cards, other.all_cards):
                if card_self != card_other:
                    return card_self < card_other
        return False


if __name__ == "__main__":
    all_hands = []
    for hand in inputs:
        all_hands.append(Hand(hand.split()[0], hand.split()[1]))

    sorted_hand_objects = sorted(all_hands, reverse=False)

    part_2 = sum([hand.bet * (c+1) for c, hand in enumerate(sorted_hand_objects)])
    print(part_2)