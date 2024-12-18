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

    def traverse_and_count_edges(expanded_grid):
        def _traverse_one_perimeter(curr, visited_edges, expanded_grid):
            out = 0
            prev_dir = None
            while curr:
                visited_edges.add(curr)
                curr, d = find_next_edge(curr, visited_edges, expanded_grid)

                if d is not None and d != prev_dir:
                    out += 1
                prev_dir = d

            return out

        visited_edges = set()
        total = 0
        # find first edge
        for i, row in enumerate(expanded_grid):
            for j, cell in enumerate(row):
                if cell == 1 and (i, j) not in visited_edges:
                    total += _traverse_one_perimeter((i, j), visited_edges, expanded_grid)

        return total

    def find_next_edge(curr_edge, visited_edges, g):
        dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        for i, d in enumerate(dirs):
            n = add_tuples(curr_edge, d)
            if not is_out_of_bound(n, g) and n not in visited_edges and g[n[0]][n[1]] == 1:
                return n, i

        return None, None

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

        for r in expanded_grid:
            print(r)
        perimeter = traverse_and_count_edges(expanded_grid)
        print(perimeter)

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
    with open("test_input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
