import numpy as np


def is_valid_reflection(i, grid) -> bool:
    l, r = i, i + 1
    total_diff = 0
    while l >= 0 and r < len(grid):
        total_diff += sum(abs(grid[l] - grid[r]))
        l -= 1
        r += 1

    return total_diff == 1


def get_reflection(grid):
    for i in range(len(grid)):
        if is_valid_reflection(i, grid):
            return i + 1
    return 0


def solution(input):
    grids = []
    curr = []
    for line in input:
        if line == "":
            grids.append(np.array(curr))
            curr = []
        else:
            curr.append(list(map(lambda x: 1 if x == "#" else 0, line)))
    grids.append(np.array(curr))

    out = 0
    for grid in grids:
        rows = get_reflection(grid)
        cols = get_reflection(grid.T)
        out += 100 * rows + cols

    return out


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))  # 36771
