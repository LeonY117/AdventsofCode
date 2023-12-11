from utils.utils import add, invert, isWithinBounds, isOnBound, print_grid

# the mapping from letter to [x, y] <-> [x, y]
left, right, down, up = (-1, 0), (1, 0), (0, 1), (0, -1)
lookup = {
    "|": (down, up),
    "-": (left, right),
    "L": (up, right),
    "J": (up, left),
    "7": (left, down),
    "F": (down, right),
}


def getLoop(grid):
    visited = [[False for _ in line] for line in grid]

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
                return cell
        return None

    def adjust_start(start, neighbors):
        neighbors = [add(neighbors[0], invert(start)), add(neighbors[1], invert(start))]
        for letter, directions in lookup.items():
            if {*neighbors} == {*directions}:
                grid[start[1]][start[0]] = letter

    start = find_start()
    neighbors = get_valid_neighbors(start)
    adjust_start(start, neighbors)
    curr = neighbors[0]
    visited[start[1]][start[0]] = True

    # unlike part1, here we just keep 1 item to iterate to next
    while curr:
        x, y = curr
        if not visited[y][x]:
            curr = bfs((x, y))
        visited[y][x] = True

    return visited


def solution(input):
    """
    Idea: shoot a ray from any point, and count the number of times it crosses the boundary,
    if the count is even, it's outside the shape, if it's odd, it's inside the shape

    Edge case (for this input it's actually MOST of the time):
    If a ray happen to be travelling adjacent and on a border:
    we count 2 if the perpendicular tips of the border point in the same direction
    we count 1 if the perpendicular tips of the border point in the opposite direction
    I.e.
    counts as 2:  F--     counts as 1:  --7
                  |                       |
                  |                       |
                  L--                     L--

                  ^                       ^
                 ray                     ray
    """
    grid = [[cell for cell in line] for line in input]
    inside = [[False for _ in line] for line in input]

    loop = getLoop(grid)

    # a set containing all the non-loop cells
    dots = set()
    for j, row in enumerate(grid):
        for i, cell in enumerate(row):
            if not loop[j][i]:
                dots.add((i, j))
                grid[j][i] = "."

    opposites = {"J": "7", "F": "L", "L": "F", "7": "J"}
    for dot in dots:
        x, y = dot

        count = 0
        start = None
        # shoot a ray upwards
        for j in range(0, y):
            ray = grid[j][x]
            crossed = 0
            if ray == "-":
                start = None
                crossed = 1
            elif ray in ["J", "F", "L", "7"]:
                if opposites[ray] == start or not start:
                    crossed = 1
                # reset start
                start = ray if not start else None
            count += crossed
        inside[y][x] = count % 2
        grid[y][x] = str(count)

    return sum(sum(row) for row in inside)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
