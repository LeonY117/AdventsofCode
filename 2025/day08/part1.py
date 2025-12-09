from utils import *


class Node:
    def __init__(self, coord):
        self.coord = coord
        self.neighbors = set()

    def add_neighbor(self, neighbor):
        self.neighbors.add(neighbor)

    def __str__(self):
        return f"Node{self.coord}"


def cartesian_distance(c1, c2):
    return (c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2 + (c1[2] - c2[2]) ** 2


def create_distance_to_pair_map(coords):
    out = {}
    for i, c1 in enumerate(coords):
        for j, c2 in enumerate(coords):
            if i == j:
                continue
            d = cartesian_distance(c1, c2)
            if d in out and out[d][0] != c2:
                raise ValueError("Contains duplicate distance")
            out[d] = (c1, c2)
    return out


def traverse_and_get_group_sizes(nodes):
    remaining = set(nodes.keys())
    group_sizes = []
    while remaining:
        queue = [next(iter(remaining))]
        group_size = 0
        while queue:
            c = queue.pop()
            if c not in remaining:
                continue
            queue += [n.coord for n in nodes[c].neighbors]
            remaining.remove(c)
            group_size += 1
        group_sizes.append(group_size)
    return group_sizes


def solution(inp):
    coords = [l.split(",") for l in inp]
    coords = [(int(c[0]), int(c[1]), int(c[2])) for c in coords]
    nodes = {c: Node(c) for c in coords}
    distance_to_pair_map = create_distance_to_pair_map(coords)

    # sort distance by ascending order and go through the pairs.
    for d in sorted(distance_to_pair_map.keys())[:1000]:
        c1, c2 = distance_to_pair_map[d]
        nodes[c1].add_neighbor(nodes[c2])
        nodes[c2].add_neighbor(nodes[c1])

    group_sizes = sorted(traverse_and_get_group_sizes(nodes), reverse=True)
    return group_sizes[0] * group_sizes[1] * group_sizes[2]


if __name__ == "__main__":
    lines = get_input_for_day(8)
    # lines = get_file_for_day(8, "test_input")
    print(solution(lines))
