# some kind of flooding idea? we hold current and propagte a stack until either something reaches the edge,
# or it runs out of new cells and we get an enclosed area

# the mapping from letter to [x, y] <-> [x, y]
left, right, down, up = (-1, 0), (1, 0), (0, 1), (0, -1)
lookup = {
    "|": (down, up),
    "-": (left, right),
    "L": (up, right),
    "J": (up, left),
    "7": (left, down),
    "F": (down, right),
    "S": ((0, 0), (0, 0)),
    ".": ((0, 0), (0, 0)),
}


def add(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])


def invert(coord):
    return (-coord[0], -coord[1])


def isWithinBounds(coord, grid):
    return 0 <= coord[0] < len(grid[0]) and 0 <= coord[1] < len(grid)


def isOnBound(coord, grid):
    return (
        coord[0] == 0
        or coord[0] == len(grid[0]) - 1
        or coord[1] == 0
        or coord[1] == len(grid) - 1
    )


def part1(input):
    grid = [[cell for cell in line] for line in input]
    isLoop = [[False for _ in line] for line in input]

    def get_start_cell_neighbors(x, y):
        out = []
        for dir in [left, right, down, up]:
            neighbor = (x + dir[0], y + dir[1])
            if not isWithinBounds(neighbor, grid):
                continue
            letter = grid[neighbor[1]][neighbor[0]]
            connections = lookup[letter]
            for i in range(2):
                source = add(connections[i], neighbor)
                # dest = add(invert(connections[(i + 1) % 2]), neighbor)
                if source == (x, y):
                    out.append(neighbor)
        return out

    def bfs(x, y):
        """
        appends the connected cell to stack if it's not visited,
        there will always be one redundant check
        """
        connections = lookup[grid[y][x]]
        for i in range(2):
            dest = add(connections[i], (x, y))
            # dest = add(invert(connections[(i + 1) % 2]), (x, y))
            if isWithinBounds(dest, grid):
                return [dest]
        return []

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "S":
                stack = get_start_cell_neighbors(x, y)
                isLoop[y][x] = True
                break
        else:
            continue
        break

    # BFS
    next = []
    steps = 0
    while stack:
        x, y = stack.pop(0)
        # print(grid[y][x])
        if not isLoop[y][x]:
            isLoop[y][x] = True
            next.extend(bfs(x, y))

        if not stack:
            steps += 1
            stack = next.copy()
            next = []

    return isLoop


def solution(input):
    grid = [[cell for cell in line] for line in input]
    isLoop = [[False for cell in line] for line in input]
    # isLoop = part1(input)

    dots = set()
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == ".":
                dots.add((i, j))

    def check_contained_and_get_neighbors(x, y):
        neighbors = []
        isContained = True
        for check_dir in [left, right, up, down]:
            coord = add((x, y), check_dir)
            if not isWithinBounds(coord, grid):
                continue
            if isOnBound(coord, grid):
                isContained = False
            letter = grid[coord[1]][coord[0]]
            if letter == "." and coord in dots:
                neighbors.append(coord)
            elif letter != ".":
                # check if the letter points back at the cell
                directions = lookup[letter]
                for dir in directions:
                    if invert(dir) == check_dir:
                        isContained = False
        return isContained, neighbors

    out = 0
    curr_count = 0
    curr_is_contained = True
    # to_visit should to be a set to avoid duplications
    to_visit = {dots.pop()}
    while len(to_visit) != 0:
        dot = to_visit.pop()
        curr_count += 1
        isContained, neighbors = check_contained_and_get_neighbors(*dot)
        curr_is_contained = curr_is_contained and isContained
        for n in neighbors:
            to_visit.add(n)
            dots.discard(n)

        # move a new dot to queue, and tally up counts
        if not to_visit:
            print(curr_count, curr_is_contained)
            out += curr_count * curr_is_contained
            curr_count, curr_is_contained = 0, True
            if dots:
                to_visit.add(dots.pop())

    return out


if __name__ == "__main__":
    with open("test.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
