import copy
from collections import defaultdict


def solution(inp):
    def blink(n):
        '''Returns a list of (num, count)'''
        if n == 0:
            return [(1, 1)]
        elif len(str(n)) % 2 == 0:
            n_str = str(n)
            l, r = int(n_str[: len(n_str) // 2]), int(n_str[len(n_str) // 2 :])
            if l == r:
                return [(l, 2)]
            return [(l, 1), (r, 1)]
        else:
            return [(n * 2024, 1)]

    # Populate the graph.
    nums = [int(n) for n in inp[0].split(" ")]
    graph = defaultdict(set)
    for num in nums:
        queue = [((num, 1), None)]
        while queue:
            (curr, count), src = queue.pop(0)
            if src is not None:
                graph[src].add((curr, count))
            children = blink(curr)
            for child in children:
                if curr not in graph.keys():
                    queue.append((child, curr))

    curr_count = {k: 1 if k in nums else 0 for k in graph.keys()}
    # Blink the graph!
    for _ in range(75):
        next_count = defaultdict(int)
        for k, v in curr_count.items():
            if v != 0:
                for n, c in list(graph[k]):
                    next_count[n] += v * c
        curr_count = next_count

    return sum(curr_count.values())


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
