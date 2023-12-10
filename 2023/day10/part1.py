def solution(input):
    grid = [[cell for cell in line] for line in input]
    visited = [[False for _ in line] for line in input]
    # we need to BFS all the cells and get shortest path
    # each iteration we increase step count by 1
    # the increment for each new cell SHOULD be done synchronously

    # the mapping from letter to [x, y] <-> [x, y]
    left, right, down, up = (-1, 0), (1, 0), (0, 1), (0, -1)
    lookup = {
        "|": (down, up),
        "-": (left, right),
        "L": (up, right),
        "J": (up, left),
        "7": (left, down),
        "F": (down, right),
        ".": [(0, 0), (0, 0)],
    }

    def add(coord1, coord2):
        return (coord1[0] + coord2[0], coord1[1] + coord2[1])

    def isWithinBounds(coord):
        return 0 <= coord[0] < len(grid[0]) and 0 <= coord[1] < len(grid)

    def get_start_cell_neighbors(x, y):
        out = []
        for dir in [left, right, down, up]:
            neighbor = (x + dir[0], y + dir[1])
            if not isWithinBounds(neighbor):
                continue
            letter = grid[neighbor[1]][neighbor[0]]
            connections = lookup[letter]
            for i in range(2):
                source = add(connections[i], neighbor)
                # dest = add(invert(connections[(i + 1) % 2]), neighbor)
                if source == (x, y):
                    out.append(neighbor)
        return out

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "S":
                stack = get_start_cell_neighbors(x, y)
                visited[y][x] = True
                break
        else:
            continue
        break

    def bfs(x, y):
        """
        appends the connected cell to stack if it's not visited,
        there will always be one redundant check
        """
        connections = lookup[grid[y][x]]
        for i in range(2):
            dest = add(connections[i], (x, y))
            # dest = add(invert(connections[(i + 1) % 2]), (x, y))
            if isWithinBounds(dest) and not visited[dest[1]][dest[0]]:
                return [dest]
        return []

    # BFS
    next = []
    steps = 0
    while stack:
        x, y = stack.pop(0)
        # print(grid[y][x])
        if not visited[y][x]:
            visited[y][x] = True
            next.extend(bfs(x, y))

        if not stack:
            steps += 1
            stack = next.copy()
            next = []

    return steps


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
