from collections import defaultdict


def solution(grid):
    def is_out_of_bound(c, grid):
        return not (0 <= c[0] < len(grid) and 0 <= c[1] < len(grid[0]))

    def add_tuples(c1, c2):
        return (c1[0] + c2[0], c1[1] + c2[1])

    def get_neighbors_and_edge_dirs(c):
        # left, up, right, down
        dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        neighbors = []
        edge_dirs = []
        for i, d in enumerate(dirs):
            n = add_tuples(c, d)
            if is_out_of_bound(n, grid):
                edge_dirs.append(i)
                continue
            if grid_at(n) == grid_at(c):
                neighbors.append(n)
            else:
                edge_dirs.append(i)

        return neighbors, edge_dirs

    def grid_at(coord):
        return grid[coord[0]][coord[1]]

    visited = [[0 for _ in grid[0]] for _ in grid]

    def coord_in_expanded_grid(c):
        return (c[0] * 2 + 1, c[1] * 2 + 1)

    def get_edges_in_expanded_grid(c, dirs):
        # left, up, right, down
        edges_for_each_dir = [
            [(-1, -1), (0, -1), (1, -1)],
            [(-1, -1), (-1, 0), (-1, 1)],
            [(-1, 1), (0, 1), (1, 1)],
            [(1, -1), (1, 0), (1, 1)],
        ]
        selected_edges = set()
        for d in dirs:
            selected_edges.update(edges_for_each_dir[d])

        out = []
        for e in selected_edges:
            out.append(add_tuples(c, e))

        return out

    def count_straight_lines(g):
        total = 0
        # count horizontal:
        for i, row in enumerate(g):
            length = 0
            for j, curr in enumerate(row):
                if curr == 0:
                    length = 0
                    continue
                elif curr == 1:
                    length += 1
                if length == 3:
                    total += 1

                # Reset if at intersection
                if curr == 1:
                    # check above and below
                    above = add_tuples((i, j), (-1, 0))
                    below = add_tuples((i, j), (1, 0))
                    if (
                        not is_out_of_bound(above, g)
                        and not is_out_of_bound(below, g)
                        and g[above[0]][above[1]] == 1
                        and g[below[0]][below[1]] == 1
                    ):
                        length = 1

        # count vertical:
        for j in range(len(g[0])):
            length = 0
            for i, _ in enumerate(g):
                curr = g[i][j]
                if curr == 0:
                    length = 0
                    continue
                elif curr == 1:
                    length += 1
                if length == 3:
                    total += 1

                # Reset if at interesection
                if curr == 1:
                    # check left and right
                    left = add_tuples((i, j), (0, -1))
                    right = add_tuples((i, j), (0, 1))
                    if (
                        not is_out_of_bound(left, g)
                        and not is_out_of_bound(right, g)
                        and g[left[0]][left[1]] == 1
                        and g[right[0]][right[1]] == 1
                    ):
                        length = 1

        return total

    def bfs(coord):
        expanded_grid = [[0] * (len(grid[0]) * 2 + 1) for _ in range(len(grid) * 2 + 1)]

        area, perimeter = 0, 0
        queue = [coord]

        while queue:
            c = queue.pop(0)
            if not visited[c[0]][c[1]]:
                visited[c[0]][c[1]] = 1
                neighbors, edge_dirs = get_neighbors_and_edge_dirs(c)
                area += 1
                queue += neighbors
                edges = get_edges_in_expanded_grid(coord_in_expanded_grid(c), edge_dirs)
                for e in edges:
                    expanded_grid[e[0]][e[1]] = 1

        perimeter = count_straight_lines(expanded_grid)

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
        lines = [l.strip() for l in f.readlines()]  # 870333 wrong

    print(solution(lines))
