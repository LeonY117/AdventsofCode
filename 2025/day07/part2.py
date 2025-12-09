from utils import *
from collections import defaultdict


def solution(inp):
    grid = [[c for c in line] for line in inp]
    num_splits = 0
    # track indices where the beam is at
    beams = set([len(grid[0]) // 2])
    beam_to_count_map = {list(beams)[0]: 1}
    for line in grid[1:]:
        new_beams, new_map = [], defaultdict(int)
        for b in beams:
            if line[b] == "^":
                new_beams += [b - 1, b + 1]
                new_map[b - 1] += beam_to_count_map[b]
                new_map[b + 1] += beam_to_count_map[b]
                num_splits += 1
            else:
                new_beams += [b]
                new_map[b] += beam_to_count_map[b]
        beams = set(new_beams)
        beam_to_count_map = new_map.copy()

    return sum(beam_to_count_map.values())


if __name__ == "__main__":
    lines = get_input_for_day(7)
    # lines = get_file_for_day(7, "test_input")
    print(solution(lines))
