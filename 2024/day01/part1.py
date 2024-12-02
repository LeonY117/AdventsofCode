def solution(inp):
    list1, list2 = [], []
    for pair in inp:
        n1, n2 = pair.split()
        list1.append(int(n1))
        list2.append(int(n2))

    list1.sort()
    list2.sort()

    return sum(abs(n1 - n2) for n1, n2 in zip(list1, list2))


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
