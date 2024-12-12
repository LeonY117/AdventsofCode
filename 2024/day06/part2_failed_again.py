def solution(grid):
    def will_turn(dir_idx_1, dir_idx_2):
        return dir_idx_2 == (dir_idx_1 + 1) % 4

    def move_in_dir(curr, dir):
        return [curr[0] + dir[0], curr[1] + dir[1]]

    def is_out_of_bound(coord):
        return not (0 <= coord[0] < len(grid) and 0 <= coord[1] < len(grid))

    # up, right, down, left
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    curr_dir_idx = 0

    # Each cell stores the previously visited direction.
    history = []
    for _ in grid:
        row = []
        for _ in grid:
            row.append([0, 0, 0, 0])
        history.append(row)

    obstacles = [[0] * len(grid[0]) for _ in grid]

    # Find guard
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                history[i][j][0] += 1
                curr = [i, j]

    while True:
        prev = curr.copy()
        prev_dir_idx, next_dir_idx = (curr_dir_idx - 1) % 4, (curr_dir_idx + 1) % 4
        prev_dir, curr_dir, next_dir = (
            dirs[prev_dir_idx],
            dirs[curr_dir_idx],
            dirs[next_dir_idx],
        )
        # move one step
        curr = move_in_dir(curr, dirs[curr_dir_idx])
        
        if is_out_of_bound(curr):
            break
        if grid[curr[0]][curr[1]] == "#":
            curr = prev.copy()
            curr_dir_idx = next_dir_idx
            # print("TURN")
            continue
        history[curr[0]][curr[1]][curr_dir_idx] += 1

        # # populate paths that will lead back here.
        # dir_idx_into_curr = prev_dir_idx
        # dir_away_from_curr = next_dir
        # c = move_in_dir(curr.copy(), dir_away_from_curr)
        # while not is_out_of_bound(c) and grid[c[0]][c[1]] != "#":
        #     history[c[0]][c[1]][dir_idx_into_curr] += 1
        #     c = move_in_dir(c, dir_away_from_curr)

        # check if an obstacle can be placed ahead.
        o = move_in_dir(curr, curr_dir)
        if is_out_of_bound(o) or grid[o[0]][o[1]] == "#" or obstacles[o[0]][o[1]] == 1:
            # print(o, 'CANT PALCE OBASTALE')
            continue

        # check if a loop will be formed if we turn here.
        c = curr.copy()
        p = c.copy()
        forms_loop = False
        while not is_out_of_bound(c):
            if grid[c[0]][c[1]] == "#":
                # Edge case: check if turn can happen at dead end.
                if history[p[0]][p[1]][(next_dir_idx+1)%4] >= 1:
                    forms_loop = True
                break
            if history[c[0]][c[1]][next_dir_idx] >= 1:
                forms_loop = True
                # print('found loop')
                break
            p = c.copy()
            c = move_in_dir(c, next_dir)
            

        if forms_loop:
            obstacles[o[0]][o[1]] = 1
            # for r in obstacles:
            #     print(r)
            # print()

    # print(obstacles)
    return sum([sum(r) for r in obstacles])


if __name__ == "__main__":
    # with open("./2024/day06/test_input.txt", "r") as f:
    with open("test_input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))  # 689 too low
