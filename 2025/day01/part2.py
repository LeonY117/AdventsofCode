def sign(n):
    return (n > 0) - (n < 0)


def crossed_zero(a, b):
    return b >= 100 > a or b <= 0 < a


def solution(inp):
    curr = 50
    count = 0
    for turn in inp:
        delta = int(turn[1:]) if turn.startswith("R") else -int(turn[1:])
        # count number of full turns
        full_turns = abs(delta) // 100

        # calculate effective turn from curr
        delta = delta - sign(delta) * full_turns * 100

        count += full_turns
        if crossed_zero(curr, curr + delta):
            count += 1

        curr = (curr + delta) % 100

    return count


if __name__ == "__main__":
    with open("dana.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
