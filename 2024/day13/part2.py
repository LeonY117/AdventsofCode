import math
import re


def solution(inp):
    machines = []
    curr_machine = []
    for line in inp:
        if line == "":
            machines.append(curr_machine)
            curr_machine = []
        else:
            curr_machine.append(line)
    machines.append(curr_machine)

    out = 0
    for machine in machines:
        x_a, y_a = re.findall(r"(\d+)", machine[0])
        x_b, y_b = re.findall(r"(\d+)", machine[1])
        x_target, y_target = re.findall(r"(\d+)", machine[2])

        a1, a2, b1, b2 = int(x_a), int(y_a), int(x_b), int(y_b)
        c1, c2 = int(x_target) + 10000000000000, int(y_target) + 10000000000000
        # c1, c2 = int(x_target), int(y_target)

        det = 1 / (a1 * b2 - a2 * b1)

        x = det * (b2 * c1 - b1 * c2)
        y = det * (-a2 * c1 + a1 * c2)

        # check that x and y are integers
        if x > 0 and y > 0 and abs(round(x) - x) < 1e-2 and abs(round(y) - y) < 1e-2:
            out += 3 * round(x) + round(y)

    return out


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
