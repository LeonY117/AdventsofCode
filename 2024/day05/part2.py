from collections import defaultdict


def solution(rules, updates):
    def sort_numbers(nums, left, right):
        if not nums:
            return []
        num = nums.pop(0)
        # Unsorted left and right
        l = [n for n in nums if n in left[num]]
        r = [n for n in nums if n in right[num]]
        return [*sort_numbers(l, left, right), num, *sort_numbers(r, left, right)]

    smaller_than, larger_than = defaultdict(list), defaultdict(list)
    for rule in rules:
        l, r = rule.split("|")
        larger_than[l].append(r)
        smaller_than[r].append(l)

    updates = [u.split(",") for u in updates]

    total = 0
    for page_numbers in updates:
        for i, num in enumerate(page_numbers):
            if all([n in larger_than[num] for n in page_numbers[i + 1 :]]):
                continue
            else:
                sorted_numbers = sort_numbers(page_numbers, smaller_than, larger_than)
                total += int(sorted_numbers[len(page_numbers) // 2])
                break
    return total


if __name__ == "__main__":
    rules, nums = [], []
    idx, all_lines = -1, []
    with open("input.txt", "r") as f:
        for i, line in enumerate(f.readlines()):
            if line.strip() == "":
                idx = i
            all_lines.append(line.strip())

    print(solution(all_lines[:idx], all_lines[idx + 1 :]))  # 6336
