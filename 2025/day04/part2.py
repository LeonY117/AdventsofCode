from utils import *


def is_valid_idx(x, y, grid):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def count_neighbors(x, y, grid):
    neighbors = [
        (x, y - 1),
        (x, y + 1),
        (x - 1, y - 1),
        (x - 1, y),
        (x - 1, y + 1),
        (x + 1, y - 1),
        (x + 1, y),
        (x + 1, y + 1),
    ]
    count = 0
    for n in neighbors:
        if not is_valid_idx(n[0], n[1], grid):
            continue
        if grid[n[1]][n[0]] == "@":
            count += 1

    return count


def solution(inp):
    grid = [list(r) for r in inp]
    count = 0

    to_remove = []
    while True:
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] != "@":
                    continue
                if count_neighbors(x, y, grid) < 4:
                    to_remove.append((x, y))
        if len(to_remove) == 0:
            break

        for x, y in to_remove:
            grid[y][x] = "."

        count += len(to_remove)
        to_remove = []

    return count


if __name__ == "__main__":
    lines = get_input_for_day(4)
    # lines = get_file_for_day(4, "test_input")
    print(solution(lines))
