from collections import defaultdict


def solution(grid):
    def is_out_of_bound(c):
        return not (0 <= c[0] < len(grid) and 0 <= c[1] < len(grid[0]))

    def add_tuples(c1, c2):
        return (c1[0] + c2[0], c1[1] + c2[1])

    def get_neighbors(c):
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for d in dirs:
            n = add_tuples(c, d)
            if is_out_of_bound(n):
                continue
            if grid_at(n) == grid_at(c):
                neighbors.append(n)

        return neighbors

    def is_edge(c):
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for d in dirs:
            n = add_tuples(c, d)
            if is_out_of_bound(n):
                return True
            if grid_at(n) != grid_at(c):
                return True
        return False

    def get_edge_neighbor(c, v):
        """Return neighbors that are unvisited and are edges."""
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for d in dirs:
            n = add_tuples(c, d)
            if is_out_of_bound(n):
                continue
            if grid_at(n) == grid_at(c) and is_edge(n) and v[n[0]][n[1]] == 0:
                return n, d

        # if not perpendicular neighbors, look for diagonal neighbors
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        for d in dirs:
            n = add_tuples(c, d)
            if is_out_of_bound(n):
                continue
            if grid_at(n) == grid_at(c) and is_edge(n) and v[n[0]][n[1]] == 0:
                return n, d

        return None, None

    def get_num_edges(c):
        out = 0
        v = [[0 for _ in grid[0]] for _ in grid]
        curr = c
        # # move to an edge if not already an edge
        # while not is_edge(c):
        #     print("not edge")
        #     c = add_tuples(c, (0, -1))
        while curr is not None:
            edge_neighbors = get_edge_neighbor(c, v)
            
        return out

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
                neighbors = get_neighbors(c)
                area += 1
                queue += neighbors

        perimeter = get_num_edges(coord)

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
