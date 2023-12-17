from typing import Tuple, Union, List

right, up, left, down = (1, 0), (0, -1), (-1, 0), (0, 1)
directions = [left, right, up, down]


def reflect_ray(mirror: str, ray: Tuple) -> Tuple:
    reflections = {
        "\\": {right: down, up: left, left: up, down: right},
        "/": {right: up, up: right, left: down, down: left},
    }
    return reflections[mirror][ray]


def split_ray(splitter: str, ray: Tuple) -> List[Tuple]:
    if (splitter == "-" and ray[1] == 0) or (splitter == "|" and ray[0] == 0):
        return [ray]

    if splitter == "-":
        return [left, right]
    elif splitter == "|":
        return [up, down]


def ray_terminates(cell: Tuple, ray: Tuple, visited_states: List[List[str]]) -> bool:
    x, y = cell
    w, h = len(visited_states[0]), len(visited_states)
    if x < 0 or y < 0 or x >= w or y >= h:
        return True
    if visited_states[y][x][ray]:
        return True

    return False


def add(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])


def get_total_cells(grid, start_state):
    visited_states = [[{d: False for d in directions} for _ in line] for line in grid]
    visited = [[False for _ in line] for line in grid]

    stack = [start_state]

    while stack:
        ray, coord = stack.pop(0)
        # print(ray, coord)
        x, y = coord
        if ray_terminates(coord, ray, visited_states):
            continue
        visited_states[y][x][ray] = True
        visited[y][x] = True
        cell = grid[y][x]
        # print(cell)
        if cell in ["-", "|"]:
            rays = split_ray(cell, ray)
            # print(rays)
            for r in rays:
                stack.append((r, add(coord, r)))
        elif cell in ["/", "\\"]:
            r = reflect_ray(cell, ray)
            stack.append((r, add(coord, r)))
        else:
            stack.append((ray, add(coord, ray)))

    return sum([sum(line) for line in visited])


def solution(input):
    grid = [[cell for cell in line] for line in input]

    max_energized = 0
    for y in range(len(grid)):
        energized = get_total_cells(grid, (right, (0, y)))
        max_energized = max(energized, max_energized)

        energized = get_total_cells(grid, (left, (len(grid) - 1, y)))
        max_energized = max(energized, max_energized)

    for x in range(len(grid[0])):
        energized = get_total_cells(grid, (down, (x, 0)))
        max_energized = max(energized, max_energized)

        energized = get_total_cells(grid, (up, (x, len(grid[0]) - 1)))
        max_energized = max(energized, max_energized)

    return max_energized


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))  # 7313
