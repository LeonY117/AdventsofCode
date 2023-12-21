import matplotlib.pyplot as plt


def add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])


def mult(k, v):
    return (k * v[0], k * v[1])


def flood_fill(grid, start):
    queue = [start]

    while queue:
        node = queue.pop()
        grid[node[1]][node[0]] = 1
        for direction in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            n = add(node, direction)
            if (
                0 <= n[0] < len(grid[0])
                and 0 <= n[1] < len(grid)
                and grid[n[1]][n[0]] == 0
            ):
                queue.append(n)


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

    curr = (-l, -t)
    grid[-t][-l] = 1
    for d, n in enumerate(instructions):
        for _ in range(n):
            curr = add(curr, directions[d])
            grid[curr[1]][curr[0]] = 1

    flood_fill(grid, (100, 100))
    plt.imshow(grid)
    plt.show()

    return sum([sum(row) for row in grid])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
