def solution(inp):
    def tally_points(count, curr_idx, v):
        indices = list(range(curr_idx, curr_idx + count))
        return sum([v * i for i in indices])

    nums = [int(n) for n in inp]
    # one pass to get the starting index at every space and file.
    starting_indices = [sum(nums[:i]) for i in range(len(nums))]

    # We go from right to left and move every group of numbers to the left.
    total = 0
    for r in range(len(nums) - 1, 0, -2):
        v = r // 2
        file_moved = False
        filesize = nums[r]
        for l in range(1, r, 2):
            # file fits in space:
            if nums[l] >= filesize:
                total += tally_points(filesize, starting_indices[l], v)
                # The empty space index is now more to the right.
                starting_indices[l] += filesize
                # Less empty space now.
                nums[l] -= filesize
                file_moved = True
                break
        if not file_moved:
            total += tally_points(filesize, starting_indices[r], v)
    return total


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        line = f.readlines()[0].strip()

    print(solution(line))  # 6415163624282
