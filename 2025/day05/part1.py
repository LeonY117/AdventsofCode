from utils import *

def id_is_in_range(i, id_ranges):
    for id_range in id_ranges:
        l, r = int(id_range[0]), int(id_range[1])
        if l <= int(i) <= r:
            return True
    return False

def solution(inp):
    id_ranges, ids = inp
    id_ranges = [r.split("-") for r in id_ranges]
    count = 0
    for i in ids:
        if id_is_in_range(i, id_ranges):
            count += 1
    return count

if __name__ == "__main__":
    lines = get_input_for_day(5, split_chunks=True)
    # lines = get_file_for_day(5, "test_input", split_chunks=True)
    print(solution(lines))
