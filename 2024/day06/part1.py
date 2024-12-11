def solution(inp):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_idx = 0
    grid = [c for c in inp]
    visited = [[0] * len(grid[0]) for _ in grid]
    # Find guard
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                visited[i][j] = 1
                curr = [i, j]

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
            visited[curr[0]][curr[1]] = 1
        if not out_of_zone:
            visited[curr[0]][curr[1]] = 0
        curr = prev.copy()
        dir_idx = (dir_idx + 1) % 4

    return sum([sum(r) for r in visited])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
