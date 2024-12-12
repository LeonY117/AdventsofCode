# O(n) did not work sadly, don't know what the edge case is, maybe I'll come back to it.
def solution(inp):
    total_success = len(inp)

    def is_increasing(n):
        return 1 <= n <= 3

    def is_decreasing(n):
        return -3 <= n <= -1

    for line in inp:
        nums = [int(s) for s in line.split()]
        diffs = [b - a for a, b in zip(nums[:-1], nums[1:])]

        failed_ups = [1 - int(is_increasing(d)) for d in diffs]
        failed_downs = [1 - int(is_decreasing(d)) for d in diffs]

        # if sum(failed_ups) >= 2 and sum(failed_downs) >= 2:
        #     total_success -= 1
        #     continue
        # elif sum(failed_ups) <= 1 or sum(failed_downs) <= 1:
        #     continue

        # ups, downs = failed_ups[0], failed_downs[0]
        num_up_fails = 1 - int(is_increasing(diffs[0]))
        num_down_fails = 1 - int(is_decreasing(diffs[0]))
        has_merged_up, has_merged_down = False, False
        for i in range(1, len(diffs)):
            if not is_increasing(diffs[i]):
                if has_merged_up:
                    num_up_fails += 1
                # for numbers a, b, c, c - a = (c - b) + (b - a)
                elif (not is_increasing(diffs[i - 1])) and is_increasing(
                    diffs[i] + diffs[i - 1]
                ):
                    num_up_fails -= 1
                    has_merged_up = True
                else:
                    num_up_fails += 1
            if not is_decreasing(diffs[i]):
                if has_merged_down:
                    num_down_fails += 1
                # for numbers a, b, c, c - a = (c - b) + (b - a)
                elif (not is_decreasing(diffs[i - 1])) and is_decreasing(
                    diffs[i] + diffs[i - 1]
                ):
                    num_down_fails -= 1
                    has_merged_down = True
                else:
                    num_down_fails += 1
            if num_up_fails >= 2 and num_down_fails >= 2:
                total_success -= 1
                break
    return total_success


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))

# 0, 6, 3, 5
