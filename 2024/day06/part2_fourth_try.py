# SO IT SEEMS LIKE BRUTE FORCE IS THE ONLY CHOICE AHHHH
def solution(grid):
    grid = [[g for g in row] for row in grid]

    def will_form_loop(curr, dir_idx, o):
        c = curr.copy()
        for _ in range(len(grid) * len(grid)):
            p = c.copy()
            c[0] += dirs[dir_idx][0]
            c[1] += dirs[dir_idx][1]
            if is_out_of_bound(c):
                return False
            if grid[c[0]][c[1]] == "#" or (c[0] == o[0] and c[1] == o[1]):
                c = p.copy()
                dir_idx = (dir_idx + 1) % 4
                continue
        return True

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
    
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            o = [i, j]
            if i == guard[0] and j == guard[1]:
                continue
            if will_form_loop(guard, 0, o):
                total += 1

    return total


if __name__ == "__main__":
    with open("./2024/day06/input.txt", "r") as f:
        # with open("test_input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))  # 1796
