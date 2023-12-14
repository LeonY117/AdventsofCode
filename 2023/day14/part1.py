def solution(input):
    grid = [[x for x in line] for line in input]

    out = 0
    rows, cols = len(grid), len(grid[0])

    # go through row by row and just count how many spaces each 'O' need to move up by
    for x in range(cols):
        curr = rows
        for y in range(rows):
            cell = grid[y][x]
            if cell == "#":
                curr = rows - y - 1
            elif cell == "O":
                out += curr
                curr -= 1

    return out


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
