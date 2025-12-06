from utils import *


def solution(inp):
    out = 0
    for s in inp:
        for d in range(11, -1, -1):
            # search within usable range (leave d numbers)
            n = max([int(n) for n in s[: len(s) - d]])
            i = s.index(str(n))
            # update usable
            s = s[i + 1 :]
            out += n * 10**d
    return out


if __name__ == "__main__":
    lines = get_input_for_day(3)
    # lines = get_file_for_day(3, "test_input")
    print(solution(lines))

    # I might've over refactored.
