import heapdict
import copy


def subtract(u, v):
    # returns u - v
    return (u[0] - v[0], u[1] - v[1])


def get_neighbors(u, grid, prev):
    ret = []
    x, y, d, c = u
    left, up, right, down = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    valid_dirs = [left, up, right, down]
    invalid_dirs = []
    # if prev[u] and prev[u][2] == d and prev[prev[u]] and prev[prev[u]][2] == d:
    if c == 3:
        print(f"{d} is invalid")
        invalid_dirs.append(d)
    invalid_dirs.append((d + 2) % 4)

    # trace back three steps:
    # prev_dir = None
    # count = 0
    # for _ in range(2):
    #     if not prev[u]:
    #         break
    #     curr_dir = subtract(u, prev[u])
    #     u = prev[u]
    #     if curr_dir == prev_dir:
    #         # print(f"repetaed dir {curr_dir}")
    #         count += 1
    #     prev_dir = curr_dir

    # if count == 1:
    #     # print(f"{curr_dir} is invalid")
    #     valid_dirs.remove(curr_dir)

    for i, (dx, dy) in enumerate(valid_dirs):
        if i in invalid_dirs:
            continue
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid):
            continue
        count = 0 if i != d else c + 1
        ret.append((nx, ny, i, count))
    return ret


# idea: try encoding the state as (x, y, dir)
# dir is 0-3 corresponding up, right, down, left
def solution(inp):
    grid = [[int(cell) for cell in line] for line in inp]
    Q = heapdict.heapdict()
    dist = {}
    prev = {}
    end = (len(grid) - 1, len(grid[0]) - 1)
    start = (0, 0)
    # initiate states
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            for d in range(4):
                for c in range(3):
                    Q[(x, y, d, c)] = float("inf")
                    dist[(x, y, d, c)] = float("inf")
                    prev[(x, y, d, c)] = None

    for d in range(4):
        Q[(*start, d, 0)] = 0
        dist[(*start, d, 0)] = 0
        prev[(*start, d, 0)] = None

    while len(Q) > 0:
        # print(Q.popitem())
        u, u_dist = Q.popitem()
        if u_dist == float("inf"):
            # print('BEEP BEEP')
            break
        if (u[0], u[1]) == end:
            print("reached")
            break
        neighbors = get_neighbors(u, grid, prev)
        # print(u, neighbors)
        for v in neighbors:
            if v in Q:
                # print(v)
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
        # print(curr)
        visualized_grid[curr[1]][curr[0]] = arrows[curr[2]]
        out += grid[curr[1]][curr[0]]
        curr = prev[curr]

    # for line in visualized_grid:
    #     print("".join([str(n) for n in line]))

    return out


if __name__ == "__main__":
    with open("test.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))  # 686
