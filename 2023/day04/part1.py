def solution(input):
    out = 0
    for line in input:
        yours, winning = line.split(": ")[1].split("|")
        yours = set([int(n) for n in yours.split()])
        winning = set([int(n) for n in winning.split()])
        overlap = len(yours.intersection(winning))
        out += 2 ** (overlap - 1) * (overlap > 0)

    return int(out)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))  # 20667
