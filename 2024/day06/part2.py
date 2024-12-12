# SO IT SEEMS LIKE BRUTE FORCE IS THE ONLY CHOICE AHHHH
def solution(grid):
    grid = [[g for g in row] for row in grid]
    visited = [[0] * len(grid[0]) for _ in grid]
    # up, right, down, left
    DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    curr_dir_idx = 0

    obstacles = [[0] * len(grid[0]) for _ in grid]

    def move_in_dir(curr, d):
        return (curr[0] + d[0], curr[1] + d[1])

    def is_out_of_bound(coord):
        return not (0 <= coord[0] < len(grid) and 0 <= coord[1] < len(grid))

    def will_form_loop(curr, dir_idx, o):
        history = [[1] * len(grid[0]) for _ in grid]
        primes = [2, 3, 5, 7]
        c = curr
        while True:
            history[c[0]][c[1]] *= primes[dir_idx]
            p = c
            c = move_in_dir(c, DIRS[dir_idx])
            if is_out_of_bound(c):
                return False
            if history[c[0]][c[1]] % primes[dir_idx] == 0:
                return True
            if grid[c[0]][c[1]] == "#" or c[0] == o[0] and c[1] == o[1]:
                c = p
                dir_idx = (dir_idx + 1) % 4
                continue

    # Find guard
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                curr = (i, j)
                visited[i][j] = 1
                break

    while True:
        prev = curr
        next_dir_idx = (curr_dir_idx + 1) % 4
        curr_dir = DIRS[curr_dir_idx]

        # move one step
        curr = move_in_dir(curr, curr_dir)

        if is_out_of_bound(curr):
            break

        if grid[curr[0]][curr[1]] == "#":
            curr = prev
            curr_dir_idx = next_dir_idx
            continue

        o = curr
        if not visited[o[0]][o[1]] and will_form_loop(prev, curr_dir_idx, o):
            obstacles[o[0]][o[1]] = 1

        visited[curr[0]][curr[1]] = 1

    return sum([sum(r) for r in obstacles])


if __name__ == "__main__":
    with open("./2024/day06/input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))  # 1796
