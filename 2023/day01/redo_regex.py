import re


def solution1(input):
    out = 0
    for line in input:
        nums = re.findall(r"[0-9]", line)
        out += int(nums[0] + nums[-1])

    return out


def solution2(input):
    numStrings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    out = 0
    # ?= is a positive lookahead without consuming character
    pattern = r"(?=("+"|".join(numStrings + [str(n) for n in list(range(1, 10))]) + "))"
    # string to int mapping
    lookup = {s: i + 1 for i, s in enumerate(numStrings)}
    for i in range(1, 10):
        lookup[str(i)] = i

    for line in input:
        matches = re.findall(pattern, line)
        out += lookup[matches[0]]*10 + lookup[matches[-1]]
        
    return out


if __name__ == "__main__":
    filename = "input.txt"
    with open(filename, "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution1(lines))  # 55386
    print(solution2(lines)) # 54824
