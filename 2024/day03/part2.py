import re


def solution(inp):
    pattern = r"mul\((\d+),(\d+)\)"
    total = 0
    segments = "".join(inp).split("do()")
    for segment in segments:
        valid_str = segment.split("don't()")[0]
        matches = re.findall(pattern, valid_str)
        total += sum([int(m[0]) * int(m[1]) for m in matches])
    return total


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
