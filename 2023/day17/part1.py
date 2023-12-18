import heapdict


def subtract(u, v):
    # returns u - v
    return (u[0] - v[0], u[1] - v[1])


def get_neighbors(u, grid, prev):
    ret = []
    x, y = u
    left, up, right, down = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    valid_dirs = {left, up, right, down}

    # trace back three steps:
    prev_dir = None
    count = 0
    for _ in range(2):
        if not prev[u]:
            break
        curr_dir = subtract(u, prev[u])
        u = prev[u]
        if curr_dir == prev_dir:
            # print(f"repetaed dir {curr_dir}")
            count += 1
        prev_dir = curr_dir

    if count == 1:
        # print(f"{curr_dir} is invalid")
        valid_dirs.remove(curr_dir)

    for dx, dy in valid_dirs:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid):
            continue
        ret.append((nx, ny))
    return ret


# idea: try encoding the state as (x, y, dir, count)
# dir is 0-3 corresponding up, right, down, left, count is 1-3
def solution(inp):
    grid = [[int(cell) for cell in line] for line in inp]
    Q = heapdict.heapdict()
    dist = {}
    prev = {}
    end = (len(grid) - 1, len(grid[0]) - 1)
    # initiate states
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            Q[(x, y)] = float("inf")
            dist[(x, y)] = float("inf")
            prev[(x, y)] = None
            # for direction in range(3):
            #     for count in range(2):
            #         Q[(x, y, direction, count)] = float("inf")
            #         prev[(x, y, direction, count)] = float("inf")
    Q[(0, 0)] = 0
    dist[(0, 0)] = 0
    while len(Q) > 0:
        u, u_dist = Q.popitem()
        if u == end:
            print("reached")
            break
        neighbors = get_neighbors(u, grid, prev)
        for v in neighbors:
            if v in Q:
                alt = dist[u] + grid[v[1]][v[0]]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    Q[v] = alt
    out = 0
    # for debug:
    curr = prev[(end)]
    while curr is not None:
        # print(curr)
        out += grid[curr[1]][curr[0]]
        grid[curr[1]][curr[0]] = "#"
        curr = prev[curr]

    for line in grid:
        print("".join([str(n) for n in line]))
    return out


if __name__ == "__main__":
    with open("test.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
