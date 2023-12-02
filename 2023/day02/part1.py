def solution(input):
    counts = {"red": 12, "green": 13, "blue": 14}
    out = 0
    for i, game in enumerate(input):
        impossible = False
        turns = game.split(": ")[1].split("; ")
        for turn in turns:
            picks = turn.split(", ")
            for pick in picks:
                n, c = pick.split(" ")
                if int(n) > counts[c]:
                    impossible = True
        if not impossible:
            out += i + 1
    return out


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))  # 2593
