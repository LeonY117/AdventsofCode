def solution(input):
    def dfs(curr):
        next = []
        if len(curr) == 1:
            return 0
        for i in range(1, len(curr)):
            next.append(curr[i] - curr[i - 1])

        return next[-1] + dfs(next)

    out = 0
    for line in input:
        points = [int(n) for n in line.split(" ")]
        out += dfs(points) + points[-1]

    return out


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
