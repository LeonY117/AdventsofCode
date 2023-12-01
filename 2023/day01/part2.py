def solution(input):
    lookup = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    out = 0
    # list of all the readable numbers
    for line in input:
        nums = []
        for i, char in enumerate(line):
            if char.isdigit():
                nums.append(char)
                continue
            for n, numString in enumerate(lookup):
                if line[i:].startswith(numString):
                    nums.append(str(n + 1))
                    break
        out += int(nums[0] + nums[-1])

    return out


if __name__ == "__main__":
    filename = "input.txt"
    with open(filename, "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))  # 54824
