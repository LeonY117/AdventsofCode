def solution(input):
    universe = input
    # without the expansion, the number of steps it takes between two galaxies a and b is:
    # |a[1] - b[1]| + |a[0] - b[0]|, i.e. sum of diff between coords

    # Get all the galaxies
    galaxies = []
    for y, row in enumerate(universe):
        for x, cell in enumerate(row):
            if cell == "#":
                galaxies.append((x, y))

    # Get all the rows & columns without stars
    empty_cols = []
    empty_rows = []
    for y, row in enumerate(universe):
        if all([cell == "." for cell in row]):
            empty_rows.append(y)

    for x, col in enumerate(zip(*universe)):
        if all([cell == "." for cell in col]):
            empty_cols.append(x)

    out = 0
    for i, start in enumerate(galaxies):
        for j, end in enumerate(galaxies[i + 1 :]):
            s_x, s_y = start
            e_x, e_y = end

            s_x, e_x = sorted([s_x, e_x])
            s_y, e_y = sorted([s_y, e_y])

            steps = abs(s_x - e_x) + abs(s_y - e_y)

            for empty_col in empty_cols:
                if s_x < empty_col < e_x:
                    steps += int(1e6) - 1

            for empty_row in empty_rows:
                if s_y < empty_row < e_y:
                    steps += int(1e6) - 1

            out += steps

    return out


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))  # 569052586852
