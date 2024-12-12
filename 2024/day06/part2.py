def solution(inp):
    def add_obstacle(curr, last_turn, obstacles, curr_dir, grid):
        print(curr)
        if curr_dir[0] == 0:
            # traveling horizontally
            corner = [curr[0], last_turn[1]]
            # check that all cells from curr to corner is free
            for j in range(*sorted([last_turn[1], curr[1]])):
                if grid[curr[0]][j] == "#":
                    print("blocked")
                    return
        else:
            corner = [last_turn[0], curr[1]]
            for i in range(*sorted([last_turn[0], curr[0]])):
                if grid[i][curr[1]] == "#":
                    print("blocked")
                    return

        obs_coord = [corner[0] + curr_dir[0], corner[1] + curr_dir[1]]
        if not (0 <= obs_coord[0] < len(grid) and 0 <= obs_coord[1] < len(grid)):
            print("out of bound")
            return
        obstacles[obs_coord[0]][obs_coord[1]] = 1

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_idx = 0
    grid = [c for c in inp]
    obstacles = [[0] * len(grid[0]) for _ in grid]

    # Find guard
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                curr = [i, j]

    prev_three_turns = []  # queue
    out_of_zone = False
    while not out_of_zone:
        # Move in one direction until #
        while grid[curr[0]][curr[1]] != "#":
            prev = curr.copy()
            curr[0] += dirs[dir_idx][0]
            curr[1] += dirs[dir_idx][1]
            if not (0 <= curr[0] < len(grid) and 0 <= curr[1] < len(grid)):
                out_of_zone = True
                print("OUT")
                break
        curr = prev.copy()
        dir_idx = (dir_idx + 1) % 4
        if len(prev_three_turns) == 3:
            prev_three_turns.pop(0)
        prev_three_turns.append(prev)
        if len(prev_three_turns) == 3:
            add_obstacle(curr, prev_three_turns[0], obstacles, dirs[dir_idx], grid)

        # remove
        if len(prev_three_turns) == 3:
            for r in obstacles:
                print(r)
            print()
            # break

    return sum([sum(r) for r in obstacles])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
