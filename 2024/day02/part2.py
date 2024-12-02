# O(n) did not work sadly, don't know what the edge case is, maybe I'll come back to it.
def solution(inp):
    total = len(inp)
    for line in inp:
        nums = [int(s) for s in line.split()]
        diffs = [b - a for a, b in zip(nums[:-1], nums[1:])]
        ups, downs = 0, 0
        diffs = [None, *diffs, None]
        for i in range(1, len(diffs) - 1):
            l, r = diffs[i - 1], diffs[i + 1]
            if not 1 <= diffs[i] <= 3:
                ups += 1
            if not 1 <= -diffs[i] <= 3:
                downs += 1

            if ups >= 2 and downs >= 2:
                total -= 1
                break
    return total


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))

# 0, 6, 3, 5
