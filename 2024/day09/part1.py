def solution(inp):
    def tally_points(count, curr_idx, v):
        indices = list(range(curr_idx, curr_idx + count))

        return sum([v * i for i in indices])

    total = 0
    nums = [int(n) for n in inp]

    # pointers
    l, r = 0, len(nums) - 1
    # values
    a, b = 0, (len(nums) - 1) // 2
    # current index.
    i = 0

    while l <= r:
        if l == r:
            if l % 2 == 0:
                total += tally_points(nums[l], i, a)
            # If it's space we skip.
            break

        # Right side is space: always move on.
        if r % 2 == 1:
            b -= 1
            r -= 1
            continue

        # Left side is number.
        if l % 2 == 0:
            total += tally_points(nums[l], i, a)
            i += nums[l]
            l += 1
            a += 1
        # Left side is space.
        else:
            # add b
            spaces = nums[l]
            # underfit
            if nums[r] <= spaces:
                total += tally_points(nums[r], i, b)
                nums[l] -= nums[r]
                i += nums[r]
                r -= 1
            # overfits
            elif nums[r] > spaces:
                total += tally_points(spaces, i, b)
                i += spaces
                nums[r] -= spaces
                l += 1
            # fills exactly
            elif nums[r] == spaces:
                l += 1

    return total


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        line = f.readlines()[0].strip()

    print(solution(line))  # 6385338159127
