from collections import defaultdict


def solution(grid):
    def is_out_of_bound(c):
        return not (0 <= c[0] < len(grid) and 0 <= c[1] < len(grid[0]))

    def add_tuples(c1, c2):
        return (c1[0] + c2[0], c1[1] + c2[1])

    def get_neighbors_and_perimeter(c):
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        perimeter = 4
        for d in dirs:
            n = add_tuples(c, d)
            if is_out_of_bound(n):
                continue
            if grid_at(n) == grid_at(c):
                neighbors.append(n)
                perimeter -= 1

        return neighbors, perimeter

    def grid_at(coord):
        return grid[coord[0]][coord[1]]

    visited = [[0 for _ in grid[0]] for _ in grid]

    def bfs(coord):
        area, perimeter = 0, 0
        queue = [coord]

        while queue:
            c = queue.pop(0)
            if not visited[c[0]][c[1]]:
                visited[c[0]][c[1]] = 1
                neighbors, p = get_neighbors_and_perimeter(c)
                area += 1
                perimeter += p
                queue += neighbors

        return area, perimeter

    regions = defaultdict(int)
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            if not visited[i][j]:
                area, perimeter = bfs((i, j))
                region = grid_at((i, j))
                regions[region] += area * perimeter
    
    return sum(regions.values())


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
