def solution(input):
    colors = {"red": 0, "green": 1, "blue": 2}
    out = 0
    for i, game in enumerate(input):
        mins = [0, 0, 0]
        turns = game.split(": ")[1].split("; ")
        for turn in turns:
            picks = turn.split(", ")
            for pick in picks:
                n, c = pick.split(" ")
                mins[colors[c]] = max(mins[colors[c]], int(n))
        out += mins[0] * mins[1] * mins[2]
    return out


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
