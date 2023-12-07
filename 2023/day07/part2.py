from collections import Counter

CARDS = "AKQT98765432J"
CARD_VALUE = {char: i + 1 for i, char in enumerate(CARDS[::-1])}

patterns = [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [1, 1, 3], [2, 3], [1, 4], [5]]


def hand_value(hand):
    """Evaluates the value of a hand in the same category using base 13"""
    return sum([CARD_VALUE[card] * 13**i for i, card in enumerate(hand[::-1])])


def best_combo_with_joker(hand):
    """Add the number of jokers to the highest count to make the best combo"""
    cards = Counter(hand)
    if "J" in cards and len(cards) != 1:
        num_Js = cards.pop("J")
        out = sorted(cards.values())
        out[-1] += num_Js
        return out
    else:
        return sorted(cards.values())


def solution(input):
    parsed_hands = []
    for line in input:
        hand, bid = line.split(" ")
        pattern = best_combo_with_joker(hand)
        rank = patterns.index(pattern)
        value = hand_value(hand)
        parsed_hands.append((rank, value, int(bid)))

    # sort by rank first, then value
    sorted_hands = sorted(parsed_hands, key=lambda x: (x[0], x[1]))
    return sum([(i + 1) * bid for i, (_, _, bid) in enumerate(sorted_hands)])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))  # 250577259
