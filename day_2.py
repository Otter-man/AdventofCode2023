from functools import reduce
import operator


def parse_games(game_details):
    game_details = game_details.strip().split("; ")
    hands = []
    for hand in game_details:
        hand = hand.split(", ")
        hand = {i.split()[1]: int(i.split()[0]) for i in hand}
        hands.append(hand)

    return hands


LEGIT_HANDS = {"red": 12, "green": 13, "blue": 14}


class Game:
    def __init__(self, game_details):
        self.title = int(game_details.split(":")[0].split()[1])
        self.hands = parse_games(game_details.split(":")[1])
        self.valid_game = self._validate_hands()
        self.power = self._calculate_power()

    def _validate_hands(self):
        all_hands_valid = True
        for hand in self.hands:
            for color in LEGIT_HANDS:
                if color in hand and hand[color] > LEGIT_HANDS[color]:
                    all_hands_valid = False
                    return all_hands_valid

        return all_hands_valid

    def _calculate_power(self):
        minimum = {"red": 1, "green": 1, "blue": 1}
        for hand in self.hands:
            for color in minimum:
                if color in hand and hand[color] > minimum[color]:
                    minimum[color] = hand[color]
        return reduce(operator.mul, minimum.values())


def create_games_db(input_file):
    games_db = list()
    with open(input_file) as f:
        games = f.readlines()
        for game in games:

            game = Game(game)
            games_db.append(game)

    return games_db


if __name__ == "__main__":
    games_db = create_games_db("inputs/day_2_input.txt")
    legit_games_db = list()
    power_games_db = list()

    for game in games_db:
        if game.valid_game:
            legit_games_db.append(game.title)
        power_games_db.append(game.power)

    print(sum(legit_games_db))

    print(sum(power_games_db))
