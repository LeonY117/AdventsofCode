def solution(input):
    out = 0
    for i, game in enumerate(input):
        mins = {"red": 0, "green": 0, "blue": 0}
        turns = game.split(": ")[1].split("; ")
        for turn in turns:
            picks = turn.split(", ")
            for pick in picks:
                n, c = pick.split(" ")
                mins[c] = max(mins[c], int(n))
        out += mins["red"] * mins["green"] * mins["blue"]
    return out


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))  # 54699
