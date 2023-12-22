import regex
from typing import Dict


def check_inequality(letter: str, x: Dict[str, int], ineq: int, threshold: int):
    if letter == "else":
        return True
    return x[letter] < threshold if ineq == 0 else x[letter] > threshold


def solution(inp):
    workflows = {}  # {workflow: List[Tuple]}

    for i, line in enumerate(inp):
        if line == "":
            raw_workflow = inp[:i]
            ratings = inp[i + 1 :]
            break

    # Encode < as 0, > as 1, each logic is a tuple i.e. (letter, 0, 35, dest) -> <35:dest
    # for the else condition we'll do {e: dest}
    for line in raw_workflow:
        matches = regex.match(r"(.+)\{(.+)\}", line)
        name = matches.group(1)
        checks = matches.group(2).split(",")
        workflows[name] = []
        for check in checks[:-1]:
            condition, destination = check.split(":")
            matches = regex.match(r"(.+)([<>])(.+)", condition)
            letter, ineq, threshold = (
                matches.group(1),
                matches.group(2),
                matches.group(3),
            )
            workflows[name].append(
                (letter, int(ineq == ">"), int(threshold), destination)
            )
        workflows[name].append(("else", -1, -1, checks[-1]))

    accepted = 0
    for line in ratings:
        part = {}
        # remove curly brackets
        xmas = line[1:-1].split(",")
        for keyvalue in xmas:
            key, value = keyvalue.split("=")
            part[key] = int(value)

        curr = "in"
        while curr:
            conditions = workflows[curr]
            curr = None
            for l, ineq, thres, dest in conditions:
                # if the part passes the condition
                if check_inequality(l, part, ineq, thres):
                    if dest == "A":
                        accepted += sum(part.values())
                    elif dest == "R":
                        pass
                    else:
                        curr = dest
                    break

    return accepted


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
