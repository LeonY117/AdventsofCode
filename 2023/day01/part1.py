def solution(input):
    out = 0
    for line in input:
        nums = []
        for char in line:
            if char.isdigit():
                nums.append(char)
        out += int(nums[0] + nums[-1])

    return out


if __name__ == "__main__":
    filename = "input.txt"
    with open(filename, "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))  # 55386
