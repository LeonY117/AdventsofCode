import matplotlib.pyplot as plt


def add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])


def mult(k, v):
    return (k * v[0], k * v[1])


def solution(inp):
    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}

    # one pass to parse the data & get grid size
    l, r, t, b = 0, 0, 0, 0
    curr = (0, 0)
    instructions = []
    for line in inp:
        d, n, _ = line.split(" ")
        curr = add(curr, mult(int(n), directions[d]))
        instructions.append((d, int(n)))
        l = min(l, curr[0])
        r = max(r, curr[0])
        t = min(t, curr[1])
        b = max(b, curr[1])

    grid = [[0 for _ in range(r - l + 1)] for _ in range(b - t + 1)]

    curr = (0, 0)
    grid[0][0] = 1
    for d, n in instructions:
        for _ in range(n):
            # print(curr, )
            curr = add(curr, directions[d])
            grid[curr[1]][curr[0]] = 1

    plt.imshow(grid)
    plt.show()
    # print(len(grid), len(grid[0]))


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
