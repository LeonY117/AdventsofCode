def solution(inp):
    total = len(inp)
    for line in inp:
        nums = [int(s) for s in line.split()]
        up, down = True, True
        for i in range(len(nums) - 1):
            up = up and 1 <= nums[i + 1] - nums[i] <= 3
            down = down and 1 <= nums[i] - nums[i + 1] <= 3
            if not down and not up:
                total -= 1
                break
    return total


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))  # 269
