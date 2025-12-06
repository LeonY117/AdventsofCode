from utils import *


def num_is_invalid(n: str):
    return n[: len(n) // 2] == n[len(n) // 2 :]


def solution(inp):
    ranges = [r.split("-") for r in inp[0].split(",")]
    total = 0
    for r in ranges:
        a, b = int(r[0]), int(r[1])
        # get numbers within the range & convert to strings
        nums = [str(n) for n in range(a, b + 1)]
        # get invalid_nums and convert to integers
        invalid_nums = [int(n) for n in nums if num_is_invalid(n)]

        total += sum(invalid_nums)

    return total


if __name__ == "__main__":
    lines = get_input_for_day(2)
    # lines = get_file_for_day(2, "test_input")
    print(solution(lines))
