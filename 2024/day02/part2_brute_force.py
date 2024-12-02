def solution(inp):
    total = 0

    def all_up_or_down(nums):
        up, down = True, True
        for i in range(len(nums) - 1):
            up = up and 1 <= nums[i + 1] - nums[i] <= 3
            down = down and 1 <= nums[i] - nums[i + 1] <= 3
            if not down and not up:
                return False
        return True

    for line in inp:
        nums = [int(s) for s in line.split()]
        for i in range(len(nums)):
            if all_up_or_down(nums[:i] + nums[i + 1 :]):
                total += 1
                break

    return total


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
