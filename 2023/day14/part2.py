from typing import List
from collections import OrderedDict


def solution(input):
    grid = [[x for x in line] for line in input]
    rows, cols = len(grid), len(grid[0])
    CYCLES = 1000000000
    NUM_TRIES = 1000  # the number of iterations to find a cycle

    def tilt_grid():
        """Updates the grid inplace by swapping cells"""
        for x in range(cols):
            j = 0
            for y in range(rows):
                cell = grid[y][x]
                if cell == "#":
                    j = y + 1
                elif cell == "O":
                    grid[y][x], grid[j][x] = grid[j][x], grid[y][x]
                    j += 1

    def rotate(grid: List[List[str]]) -> List[List[str]]:
        """Rotates the 2D grid clockwise"""
        grid[:] = map(list, zip(*grid[::-1]))
        return grid

    def encode(grid: List[List[str]]) -> str:
        "Flattens the grid state"
        return "".join(["".join(line) for line in grid])

    def decode(state: str) -> List[List[str]]:
        """Reshaping the state as a string back into the 2D array"""
        # initiate empty grid
        grid = [[0 for _ in range(cols)] for _ in range(rows)]
        grid_state, rot_state = state[:-1], int(state[-1])
        for i, s in enumerate(grid_state):
            x, y = i % rows, i // rows
            grid[y][x] = s

        num_rotates = (4 - (rot_state)) % 4
        # rotate back to the original orientation
        for _ in range(num_rotates):
            grid = rotate(grid)

        return grid

    def count_beam_support(grid) -> int:
        out = 0
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == "O":
                    out += cols - y

        return out

    def print_grid(grid):
        [print("".join(row)) for row in grid]
        print("")
        return

    # --------- MAIN LOOP -----------
    # the state is a ordered dict of strings each containing the flattened grid
    # plus a number between 0-3 showing how many times it's rotated
    # each state string can be decoded back into the grid in the right orientation
    states = OrderedDict()
    rot_state = 0
    for i in range(NUM_TRIES):
        tilt_grid()
        state = encode(grid) + str(rot_state)

        # look for repeated state
        if state in states:
            start, end = states[state], i
            print(f"Found loop from {start} to {end}")
            break

        # append state & rotate grid
        states[state] = i
        grid = rotate(grid)
        rot_state = (rot_state + 1) % 4

    final_state = list(states.keys())[start + (4 * CYCLES - start - 1) % (end - start)]
    return count_beam_support(decode(final_state))


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
