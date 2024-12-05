def solution(rules, updates):
    def sort_numbers(nums, left_nums, right_nums):
        if not nums:
            return []
        unsorted_left, unsorted_right = [], []
        num = nums.pop(0)

        # sort left
        for n in nums:
            if n in left_nums[num]:
                unsorted_left.append(n)
            elif n in right_nums[num]:
                unsorted_right.append(n)
            else:
                print("THIS SHOULD NEVER HAPPEN BY CONSTRUCTION OF THIS PROBLEM.")

        sorted_left = sort_numbers(unsorted_left, left_nums, right_nums)
        sorted_right = sort_numbers(unsorted_right, left_nums, right_nums)

        return [*sorted_left, num, *sorted_right]

    larger_than_n = {}
    smaller_than_n = {}
    for rule in rules:
        l, r = rule.split("|")
        if l not in larger_than_n:
            larger_than_n[l] = [r]
        else:
            larger_than_n[l].append(r)
        if r not in smaller_than_n:
            smaller_than_n[r] = [l]
        else:
            smaller_than_n[r].append(l)

    updates = [u.split(",") for u in updates]

    total = 0
    for page_numbers in updates:
        mid = 0
        for i, num in enumerate(page_numbers):
            if all(
                [num in larger_than_n and n in larger_than_n[num] for n in page_numbers[i + 1 :]]
            ):
                continue
            else:
                sorted_numbers = sort_numbers(page_numbers, smaller_than_n, larger_than_n)
                mid = sorted_numbers[len(page_numbers) // 2]
                break
        total += int(mid)
    return total


if __name__ == "__main__":
    rules, nums = [], []
    idx, all_lines = -1, []
    with open("input.txt", "r") as f:
        for i, line in enumerate(f.readlines()):
            if line.strip() == "":
                idx = i
            all_lines.append(line.strip())

    print(solution(all_lines[:idx], all_lines[idx + 1 :]))
