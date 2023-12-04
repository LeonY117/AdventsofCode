import numpy as np


def solution(input):
    num_cards = np.array([1] * len(input))
    for i, line in enumerate(input):
        yours, winning = line.split(": ")[1].split("|")
        yours = set([int(n) for n in yours.split()])
        winning = set([int(n) for n in winning.split()])
        overlap = len(yours.intersection(winning))
        num_cards[i + 1 : i + overlap + 1] += 1 * num_cards[i]

    return sum(num_cards)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))  # 5833065
