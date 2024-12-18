from collections import defaultdict
import copy


def solution(inp):

    def blink(n):
        if n == 0:
            return [1]
        elif len(str(n)) % 2 == 0:
            n_str = str(n)
            return [int(n_str[: len(n_str) // 2]), int(n_str[len(n_str) // 2 :])]
        else:
            return [n * 2024]

    nums = [int(n) for n in inp[0].split(" ")]
    graph = defaultdict(set)

    for num in nums:
        queue = [(num, None)]
        while queue:
            curr, src = queue.pop(0)
            if src is not None:
                graph[src].append(curr)
            children = blink(curr)
            for child in children:
                if curr not in graph.keys():
                    queue.append((child, curr))

    curr_count = {k: 0 for k in graph.keys()}

    for n in nums:
        curr_count[n] = 1

    for _ in range(6):
        next_count = defaultdict(int)
        for k, v in curr_count.items():
            if v != 0:
                for n in list(graph[k]):
                    next_count[n] += v
        curr_count = next_count
    
    for _ in range(1):
        next_count = defaultdict(int)
        for k, v in curr_count.items():
            if v != 0:
                print("parent")
                print(k, v, graph[k])
                for n in list(graph[k]):
                    print(n, next_count[n])
                    next_count[n] += v
                    print(n, next_count[n])
        curr_count = next_count

    for k in sorted(list(curr_count.keys())):
        print(k, curr_count[k])
    return sum(curr_count.values())


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
