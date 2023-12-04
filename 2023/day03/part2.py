import numpy as np
import re


def solution(input):
    grid = np.array([list(line) for line in input])
    gears = [[[] for _ in row] for row in input]

    def getGear(row, l, r) -> None:
        """
        grid[row][l:r] is the word
        """
        if l == -1 or r == -1:
            return
        tocheck = []
        for i in range(l - 1, r + 1):
            tocheck.append((row - 1, i))  # top row
            tocheck.append((row + 1, i))  # bottom row
        # left and right
        tocheck.append((row, l - 1))
        tocheck.append((row, r))

        for j, i in tocheck:
            if j < 0 or j >= len(grid) or i < 0 or i >= len(grid[0]):
                continue
            if grid[j][i] == "*":
                gears[j][i].append(int("".join(grid[row][l:r])))

        return

    for i, row in enumerate(grid):
        left, right = -1, -1
        for match in re.finditer("[0-9]+", "".join(row)):
            left, right = match.start(), match.end()
            getGear(i, left, right)
    out = 0
    for row in gears:
        out += sum([g[0] * g[1] for g in row if len(g) == 2])
    return out


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))  # 84399773
