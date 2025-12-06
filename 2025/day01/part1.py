def solution(inp):
    curr = 50
    count = 0
    for turn in inp:
        delta = int(turn[1:]) if turn.startswith("R") else -int(turn[1:])
        curr = (curr + delta) % 100
        if curr == 0:
            count += 1
    return count


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
