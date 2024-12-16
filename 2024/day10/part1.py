def solution(grid):
    grid = [[int(n) for n in row] for row in grid]

    def is_out_of_bound(c):
        return not (0 <= c[0] < len(grid) and 0 <= c[1] < len(grid[0]))

    def add_tuples(c1, c2):
        return (c1[0] + c2[0], c1[1] + c2[1])

    def get_neighbors(c):
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        out = []
        for d in dirs:
            n = add_tuples(c, d)
            if not is_out_of_bound(n):
                out.append(n)
        return out

    def grid_at(coord):
        return grid[coord[0]][coord[1]]

    def dfs(coord, height, visited):
        if height == 9:
            visited[coord] = 1

        ns = get_neighbors(coord)
        for n in ns:
            if grid_at(n) == height + 1:
                dfs(n, height + 1, visited)
        return

    # one pass to get positions of all the trailheads
    trailheads = []
    hilltops = {}

    for i, row in enumerate(grid):
        for j, n in enumerate(row):
            if n == 0:
                trailheads.append((i, j))
            if n == 9:
                hilltops[(i, j)] = 0

    total = 0
    for trailhead in trailheads:
        visited = hilltops.copy()
        dfs(trailhead, 0, visited)
        total += sum(visited.values())

    return total


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
