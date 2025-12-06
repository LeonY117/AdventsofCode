from utils import *

def solution(inp):
    out = 0
    for line in inp:
        first_digit = max([int(n) for n in line[:-1]])
        first_idx = line.index(str(first_digit))
        second_digit = max([int(n) for n in line[first_idx+1:]])
        out += first_digit * 10 + second_digit

    return out

if __name__ == "__main__":
    lines = get_input_for_day(3)
    # lines = get_file_for_day(3, "test_input")
    print(solution(lines))
