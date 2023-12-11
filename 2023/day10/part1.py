from utils.utils import add, isWithinBounds


def solution(input):
    # storing all coordinates as [x, y]
    grid = [[cell for cell in line] for line in input]
    visited = [[False for _ in line] for line in input]
    # we need to BFS all the cells and get shortest path
    # each iteration we increase step count by 1
    # the increment for each new cell SHOULD be done synchronously

    # the mapping from letter to the two positions that they connect to
    left, right, up, down = (-1, 0), (1, 0), (0, -1), (0, 1)
    lookup = {
        "|": (down, up),
        "-": (left, right),
        "L": (up, right),
        "J": (up, left),
        "7": (left, down),
        "F": (down, right),
    }

    def get_valid_neighbors(coord):
        # returns the two valid neighbors that connect to x, y
        out = []
        for direction in [left, right, down, up]:
            # neighbor coordinate is [x, y] + direction
            nb = add(coord, direction)
            if not isWithinBounds(nb, grid):
                continue
            letter = grid[nb[1]][nb[0]]
            connections = lookup.get(letter, [(0, 0)])
            for connection in connections:
                source = add(connection, nb)
                # checks to see if the potential neighbor points back at the source
                if source == coord:
                    out.append(nb)
        return out

    def find_start():
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == "S":
                    return (x, y)

    def bfs(coord):
        """
        appends the connected cell to stack if it's not visited,
        (there will always be one redundant check)
        """
        x, y = coord
        connections = lookup.get(grid[y][x], [(0, 0)])
        for connection in connections:
            cell = add(connection, coord)
            if isWithinBounds(cell, grid) and not visited[cell[1]][cell[0]]:
                return [cell]
        return []

    start = find_start()
    stack = get_valid_neighbors(start)
    visited[start[1]][start[0]] = True
    # BFS: we keep a stack with 2 items, and iterate to the next step when both are visited
    next = []
    steps = 0

    while stack:
        x, y = stack.pop(0)
        if not visited[y][x]:
            next.extend(bfs((x, y)))

        if not stack:
            steps += 1
            stack = next.copy()
            next = []

        visited[y][x] = True

    return steps


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
