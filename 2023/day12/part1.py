from typing import List


def is_valid_arrangement(s: str, arrangement: List[int]) -> bool:
    """checks if given COMPLETED string is consistent the arrangement"""
    a = arrangement.copy()
    curr = 0
    for char in s:
        if char == "#":
            curr += 1
        else:
            if curr != 0 and curr != a.pop(0):
                return False
            curr = 0

    return len(a) == 0 or a[-1] == curr


def permute(num_o: int, num_d: int) -> List[str]:
    """Given the number of operational and number of damaged parts, return all permutations"""
    out = []

    def helper(curr: str, num_o: int, num_d: int) -> None:
        if num_o == 0 and num_d == 0:
            out.append(curr)
            return

        if num_o > 0:
            helper(curr + ".", num_o - 1, num_d)
        if num_d > 0:
            helper(curr + "#", num_o, num_d - 1)

    helper("", num_o, num_d)

    return out


def insert_permutation(record: str, permutation: str) -> str:
    """Given record with unknown pos and a permutation of arrangments of . and # , return the completed record"""

    record, permutation = list(record), list(permutation)
    for i, char in enumerate(record):
        if char == "?":
            record[i] = permutation.pop(0)
    return "".join(record)


def solution(input):
    # The strings are all very short, so it's possible to run through all permutations for part 1
    out = 0
    for line in input:
        record, arrangement = line.split(" ")
        arrangement = [int(n) for n in arrangement.split(",")]
        total_damaged = sum(arrangement)
        known_damaged = sum([char == "#" for char in record])
        num_question = sum([char == "?" for char in record])

        num_d = total_damaged - known_damaged
        num_o = num_question - num_d

        permutations = permute(num_o, num_d)

        for p in permutations:
            completed_record = insert_permutation(record, p)
            if is_valid_arrangement(completed_record, arrangement):
                out += 1

    return out


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines)) # 8419
