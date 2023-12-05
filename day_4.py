with open ('inputs/day_4_input.txt', "r") as f:
    all_cards = f.readlines()

import math

def solve_part_1(all_cards):
    cards_extracted = extract_cards(all_cards)
    cards_formated = format_cards(cards_extracted)
    cards_scored = score_cards(cards_formated)
    return sum([card["score"] for card in cards_scored])



def score_cards(cards_formated):
    for card in cards_formated:
        set1 = set(card["winning_numbers"])
        set2 = set(card["numbers"])
        any_winners = set1.intersection(set2)
        if any_winners:
            score = 1
            winning_cards = 0
            for number in card["numbers"]:
                if number in any_winners:
                    score = score * 2
                    winning_cards += 1
        else:
            score = 0
            winning_cards = 0
        card["score"] = score / 2
        card["card_won"] = winning_cards
        card["card_cost"] = 1

    return cards_formated

def solve_part_2(all_cards):
    cards_extracted = extract_cards(all_cards)
    cards_formated = format_cards(cards_extracted)
    cards_scored = score_cards(cards_formated)
    cards_compounded = compound_cards(cards_scored)

    return cards_compounded

def compound_cards(cards_scored):

    for card in cards_scored:
        if card["card_won"] == 0: continue

        for i in range(card["card_number"]+1, card["card_number"]+1 + card["card_won"]):
            cards_scored[i]["card_cost"] += card["card_cost"]

    return sum([card["card_cost"] for card in cards_scored])

def extract_cards(all_cards):
    cards = []
    for card in all_cards:
        card_formated = dict()
        card_formated['card_number'] = int(card.split(":")[0].split()[1].strip())-1
        card_formated['winning_numbers'] = card.split(":")[1].split("|")[0].strip()
        card_formated['numbers'] = card.split(":")[1].split("|")[1].strip()
        cards.append(card_formated)
    return cards

def format_cards(cards_extracted):
    cards = []
    for card in cards_extracted:
        card['winning_numbers'] = list(map(int, card['winning_numbers'].split()))
        card['numbers'] = list(map(int, card['numbers'].split()))
        cards.append(card)

    return cards

if __name__ == "__main__":
    score = solve_part_1(all_cards)
    print(score)
    compound = solve_part_2(all_cards)
    print(compound)