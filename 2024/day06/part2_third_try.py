# SO IT SEEMS LIKE BRUTE FORCE IS THE ONLY CHOICE AHHHH


def solution(grid):
    grid = [[g for g in row] for row in grid]
    visited = [[0] * len(grid[0]) for _ in grid]

    def will_form_loop(curr, dir_idx, o):
        history = []
        for _ in grid:
            row = []
            for _ in grid:
                row.append([0, 0, 0, 0])
            history.append(row)

        initial_coord, initial_dir_idx = curr.copy(), dir_idx
        c = curr.copy()
        while True:
            history[c[0]][c[1]][dir_idx] = 1
            p = c.copy()
            c[0] += dirs[dir_idx][0]
            c[1] += dirs[dir_idx][1]
            if is_out_of_bound(c):
                return False
            if history[c[0]][c[1]][dir_idx] == 1:
                return True
            if grid[c[0]][c[1]] == "#" or (c[0] == o[0] and c[1] == o[1]):
                c = p.copy()
                dir_idx = (dir_idx + 1) % 4
                continue

    def move_in_dir(curr, dir):
        return [curr[0] + dir[0], curr[1] + dir[1]]

    def is_out_of_bound(coord):
        return not (0 <= coord[0] < len(grid) and 0 <= coord[1] < len(grid))

    def equal(c1, c2):
        return c1[0] == c2[0] and c1[1] == c2[1]

    # up, right, down, left
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    curr_dir_idx = 0

    obstacles = [[0] * len(grid[0]) for _ in grid]

    # Find guard
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                guard = [i, j]
                visited[i][j] = 1

    curr = guard.copy()
    while True:
        prev = curr.copy()
        next_dir_idx = (curr_dir_idx + 1) % 4
        curr_dir = dirs[curr_dir_idx]

        # move one step
        curr = move_in_dir(curr, curr_dir)
        # print(curr)

        if is_out_of_bound(curr):
            # print('out of bound')
            break
        if grid[curr[0]][curr[1]] == "#":
            curr = prev.copy()
            curr_dir_idx = next_dir_idx
            # print("TURN")
            continue
        visited[curr[0]][curr[1]] = 1

        # check if an obstacle can be placed ahead.
        o = move_in_dir(curr, curr_dir)
        if (
            is_out_of_bound(o)
            or grid[o[0]][o[1]] == "#"
            or obstacles[o[0]][o[1]] == 1
            or visited[o[0]][o[1]]
        ):
            continue

        # check if a loop will be formed if we turn here.
        forms_loop = will_form_loop(curr, next_dir_idx, o)

        if forms_loop:
            obstacles[o[0]][o[1]] = 1

    # print(obstacles)
    return sum([sum(r) for r in obstacles])


if __name__ == "__main__":
    with open("./2024/day06/input.txt", "r") as f:
        # with open("test_input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))  # 1756 too high but close?
