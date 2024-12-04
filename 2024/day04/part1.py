import re


def solution(grid):
    def get_triangular_grid(g):
        top_left = ["".join([g[j][i - j] for j in range(i + 1)]) for i in range(len(g) - 1)]
        bottom_right = [
            "".join([g[len(g) - 1 - j][len(g) - 1 - i + j] for j in range(i + 1)][::-1])
            for i in range(len(g))
        ]
        return top_left + bottom_right

    def rot_grid_90(grid):
        return list("".join(l) for l in zip(*grid[::-1]))

    total = 0
    for i in range(4):
        grid = rot_grid_90(grid)
        total += sum([len(re.findall("XMAS", line)) for line in grid])

        diagonal_grid = get_triangular_grid(grid)
        total += sum([len(re.findall("XMAS", line)) for line in diagonal_grid])

    return total


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
