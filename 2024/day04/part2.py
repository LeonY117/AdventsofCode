import re


def solution(grid):
    def get_triangular_grid(g):
        top_left = [[g[j][i - j] for j in range(i + 1)] for i in range(len(g) - 1)]
        bottom_right = [
            [g[len(g) - 1 - j][len(g) - 1 - i + j] for j in range(i + 1)][::-1]
            for i in range(len(g))
        ]  # D:
        return top_left + bottom_right

    def rot_grid_90(grid):
        return list(l for l in zip(*grid[::-1]))

    def convert_grid_to_string(grid):
        return ["".join(l) for l in grid]

    grid_coords = [[(i, j) for j in range(len(grid))] for i in range(len(grid))]
    hashmap = {c: 0 for l in grid_coords for c in l}
    for i in range(4):
        diagonal_grid = convert_grid_to_string(get_triangular_grid(grid))
        diagonal_coords = get_triangular_grid(grid_coords)

        for line, coords in zip(diagonal_grid, diagonal_coords):
            matches = re.finditer("MAS", line)
            for m in matches:
                coord = coords[m.start() + 1]
                hashmap[coord] += 1

        grid = convert_grid_to_string(rot_grid_90(grid))
        grid_coords = rot_grid_90(grid_coords)

    return sum([c == 2 for c in hashmap.values()])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
