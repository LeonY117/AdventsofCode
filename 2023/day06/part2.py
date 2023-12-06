import math


def solution(input):
    """
    We want to solve:
       (t-x) * x > d
        tx - x^2 > d
    x^2 - tx + d < 0
    """

    def solve_quadratic(a, b, c):
        x1 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
        x2 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)

        return (x1, x2) if x1 < x2 else (x2, x1)

    t = int(input[0].split(": ")[1].replace(" ", ""))
    d = int(input[1].split(": ")[1].replace(" ", ""))

    x1, x2 = solve_quadratic(1, -t, d)
    # this is a little cheaty, but hopefully no decimal place is gonna be this small
    x1, x2 = math.ceil(x1 + 1e-8), math.floor(x2 - 1e-8)
    return x2 - x1 + 1


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
