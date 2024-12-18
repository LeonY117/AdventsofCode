from collections import defaultdict


def solution(rules, updates):
    hashmap = defaultdict(list)
    for rule in rules:
        l, r = rule.split("|")
        hashmap[l].append(r)

    updates = [u.split(",") for u in updates]
    total = 0
    for page_numbers in updates:
        mid = page_numbers[len(page_numbers) // 2]
        for i, num in enumerate(page_numbers):
            if any([num not in hashmap or n not in hashmap[num] for n in page_numbers[i + 1 :]]):
                mid = 0
                break
        total += int(mid)
    return total


if __name__ == "__main__":
    idx, all_lines = -1, []
    with open("input.txt", "r") as f:
        for i, line in enumerate(f.readlines()):
            if line.strip() == "":
                idx = i
            all_lines.append(line.strip())

    print(solution(all_lines[:idx], all_lines[idx + 1 :]))
