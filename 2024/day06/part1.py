def solution(inp):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_idx = 0
    grid = inp
    visited = [[0] * len(grid[0]) for _ in grid]
    # Find guard
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                visited[i][j] = 1
                curr = [i, j]

    while True:
        # Move in one direction until #
        prev = curr.copy()
        curr[0] += dirs[dir_idx][0]
        curr[1] += dirs[dir_idx][1]
        if not (0 <= curr[0] < len(grid) and 0 <= curr[1] < len(grid)):
            break
        if grid[curr[0]][curr[1]] != "#":
            visited[curr[0]][curr[1]] = 1
        else:
            curr = prev.copy()
            dir_idx = (dir_idx + 1) % 4

    return sum([sum(r) for r in visited])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
