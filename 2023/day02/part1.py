def solution(input):
    colors = {"red": 0, "green": 1, "blue": 2}
    counts = [12, 13, 14]
    out = 0
    for i, game in enumerate(input):
        impossible = False
        turns = game.split(": ")[1].split("; ")
        for turn in turns:
            picks = turn.split(", ")
            for pick in picks:
                n, c = pick.split(" ")
                if int(n) > counts[colors[c]]:
                    impossible = True
        if not impossible:
            out += i + 1
    return out


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
