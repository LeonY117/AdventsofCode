import numpy as np


def solution(input):
    grid = np.array([list(line) for line in input])
    gears = [[[] for _ in row] for row in input]

    def getGear(row, l, r) -> None:
        """
        grid[row][l:r+1] is the word
        """
        if l == -1 or r == -1:
            return
        tocheck = []
        for i in range(l - 1, r + 2):
            tocheck.append((row - 1, i))  # top row
            tocheck.append((row + 1, i))  # bottom row
        # left and right
        tocheck.append((row, l - 1))
        tocheck.append((row, r + 1))

        for j, i in tocheck:
            if j < 0 or j >= len(grid) or i < 0 or i >= len(grid[0]):
                continue
            if grid[j][i] == "*":
                gears[j][i].append(int("".join(grid[row][l : r + 1])))

        return

    out = 0
    for j, row in enumerate(grid):
        left, right = -1, -1
        for i, letter in enumerate(row):
            if letter.isdigit():
                if left == -1:
                    left = i
                right = i
            else:
                if left != -1:
                    getGear(j, left, right)
                    left, right = -1, -1
        # edge case for last number
        getGear(j, left, right)
    
    for row in gears:
        for gear in row:
            if len(gear) == 2:
                out += gear[0] * gear[1]
    return out


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))  # 528898 too high
