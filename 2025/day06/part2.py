from utils import *


def prod(nums):
    out = 1
    for n in nums:
        out *= n
    return out


def solution(inp):
    for i in range(len(inp)):
        # remove line break for the rows containing numbers
        if inp[i][-1] == "\n":
            inp[i] = inp[i][:-1]

    # loop through the operations to find indices to break numbers
    num_lengths = []
    curr_length = 0
    operations = [inp[-1][0]]
    for i, o in enumerate(inp[-1]):
        if o != " " and i != 0:
            operations.append(o)
            num_lengths.append(curr_length)
            curr_length = 1
        else:
            curr_length += 1
    num_lengths.append(curr_length + 1)

    # do the actual operations
    out = 0
    p = 0  # pointer for slicing groups vertically
    for l, o in zip(num_lengths, operations):
        curr_group = []
        for i, row in enumerate(inp[:-1]):
            curr_group.append(row[p : p + l - 1])
        p += l
        # transpose & convert to integers
        curr_group = [int("".join(n)) for n in zip(*curr_group)]
        curr_total = sum(curr_group) if o == "+" else prod(curr_group)
        out += curr_total
    return out


if __name__ == "__main__":
    lines = get_input_for_day(6, strip=False)
    # lines = get_file_for_day(6, "test_input", strip=False)
    print(solution(lines))
