import re


def solution(inp):
    pattern = r"mul\((\d+),(\d+)\)"
    total = 0
    for line in inp:
        matches = re.findall(pattern, line)
        total += sum([int(m[0]) * int(m[1]) for m in matches])

    return total

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
    
    print(solution(lines))
