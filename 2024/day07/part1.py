def solution(inp):
    out = 0
    for line in inp:
        ans, nums = line.split(": ")
        ans = int(ans)
        nums = [int(n) for n in nums.split(" ")]

        all_eq = []

        def calculate_all_equations(remaining_nums, curr_val, ans):
            if curr_val > ans:
                return False
            if len(remaining_nums) == 0:
                return ans == curr_val
            else:
                n = remaining_nums[0]
                if calculate_all_equations(remaining_nums[1:], curr_val + n, ans):
                    return True
                if calculate_all_equations(remaining_nums[1:], curr_val * n, ans):
                    return True
            
            return False

        if calculate_all_equations(nums[1:], nums[0], ans):
            out += ans

    return out


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
