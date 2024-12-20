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

        x_a, y_a, x_b, y_b = int(x_a), int(y_a), int(x_b), int(y_b)
        x_target, y_target = int(x_target), int(y_target)

        # we are trying to find c1 * (x_a, y_a) + c2 * (x_b, y_b)
        c1 = 1
        minimum_cost = 9999999
        while c1 * x_a < x_target and c1 * y_a < y_target and c1 < 100:
            x_remaining = x_target - c1 * x_a
            y_remaining = y_target - c1 * y_a

            if (
                x_remaining % x_b == 0
                and y_remaining % y_b == 0
                and x_remaining // x_b == y_remaining // y_b
            ):
                c2 = y_remaining // y_b
                cost = c1 * 3 + c2
                minimum_cost = min(cost, minimum_cost)

            c1 += 1
        if minimum_cost != 9999999:
            out += minimum_cost

    return out


if __name__ == "__main__":
    with open("test_input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
