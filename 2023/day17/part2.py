import heapdict
import copy


def subtract(u, v):
    # returns u - v
    return (u[0] - v[0], u[1] - v[1])


def get_neighbors(u, grid):
    ret = []
    x, y, d, c = u
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    valid_ds = [d, d + 1, d - 1]
    if c < 4:
        valid_ds = [d]
    # the condition c > 10 doesn't need be checked because there's no such state

    for nd in valid_ds:
        nd %= 4
        dx, dy = dirs[nd]
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid):
            continue
        count = 1 if nd != d else c + 1
        ret.append((nx, ny, nd, count))
    return ret


def solution(inp):
    grid = [[int(cell) for cell in line] for line in inp]
    Q = heapdict.heapdict()
    dist, prev = {}, {}
    end = (len(grid[0]) - 1, len(grid) - 1)
    start = (0, 0)
    # initiate states
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            for d in range(4):
                for c in range(10):
                    Q[(x, y, d, c + 1)] = float("inf")
                    dist[(x, y, d, c + 1)] = float("inf")
                    prev[(x, y, d, c + 1)] = None

    # only allowed to go right and down from top left
    for d in [2, 3]:
        Q[(*start, d, 1)] = 0
        dist[(*start, d, 1)] = 0
        prev[(*start, d, 1)] = None

    while len(Q) > 0:
        u, _ = Q.popitem()
        if (u[0], u[1]) == end and u[3] >= 4:
            print("reached")
            break
        neighbors = get_neighbors(u, grid)
        for v in neighbors:
            if v in Q:
                alt = dist[u] + grid[v[1]][v[0]]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    Q[v] = alt
    out = 0
    # for debug:
    arrows = ["<", "^", ">", "v"]
    visualized_grid = copy.deepcopy(grid)
    curr = u
    while (curr[0], curr[1]) != start:
        visualized_grid[curr[1]][curr[0]] = arrows[curr[2]]
        out += grid[curr[1]][curr[0]]
        curr = prev[curr]

    # for line in visualized_grid:
    #     print("".join([str(n) for n in line]))

    return out


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))  # 801
