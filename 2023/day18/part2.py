import regex


def add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])


def mult(k, v):
    return (k * v[0], k * v[1])


def solution(input):
    coords = [(0, 0)]
    curr = (0, 0)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    area = 0
    for line in input:
        match = regex.search(r"\(#(.*?)\)", line).group(1)
        steps = int(match[:-1], 16)
        area += steps/2
        direction = directions[int(match[-1])]

        curr = add(curr, mult(steps, direction))
        coords.append(curr)

    for i in range(len(coords)):
        x1, y1 = coords[i-1]
        x2, y2 = coords[i]

        area += 1/2 * (y1 + y2) * (x1 - x2)

    return int(area) + 1

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
