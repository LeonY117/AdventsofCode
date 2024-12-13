from collections import defaultdict


def add_tuple(a, b):
    return (a[0] + b[0], a[1] + b[1])

def subtract_tuple(a, b):
    return (a[0] - b[0], a[1] - b[1])

def out_of_bound(coord, grid):
    return not (0 <= coord[0] < len(grid[0]) and 0 <= coord[1] < len(grid))

def solution(grid):
    antennas = defaultdict(list)
    antinodes = [[0] * len(grid[0]) for _ in grid]

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell != '.':
                antennas[cell].append((i, j)) 
                antinodes[i][j] = 1
    for _, antenna_coords in antennas.items():
        # for every pair:
        for i, a1 in enumerate(antenna_coords):
            for j, a2 in enumerate(antenna_coords):
                if i == j:
                    continue
                # d = a1 - a2
                d = subtract_tuple(a1, a2)
                # n = a2 - d
                n = subtract_tuple(a2, d)
                while not out_of_bound(n, grid):
                    antinodes[n[0]][n[1]] = 1
                    n = subtract_tuple(n, d)
    
    return sum([sum(r) for r in antinodes])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
    
    print(solution(lines))
