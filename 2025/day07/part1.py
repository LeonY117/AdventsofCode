from utils import *


def solution(inp):
    grid = [[c for c in line] for line in inp]
    num_splits = 0
    # track indices where the beam is at
    beams = set([len(grid[0]) // 2])
    for line in grid[1:]:
        new_beams = []
        for b in beams:
            if line[b] == "^":
                new_beams += [b - 1, b + 1]
                num_splits += 1
            else:
                new_beams += [b]
        beams = set(new_beams)
    return num_splits


if __name__ == "__main__":
    lines = get_input_for_day(7)
    # lines = get_file_for_day(7, "test_input")
    print(solution(lines))
