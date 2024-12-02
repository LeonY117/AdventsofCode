import regex
from dataclasses import dataclass


@dataclass
class Node:
    parents: set()
    conditions: []
    otherwise: str


def update_xmas(xmas, condition):
    new_xmas = xmas.copy()
    # updates the xmas intervals in-place and returns False if
    letter, ineq, threshold, _ = condition
    if ineq == 0:
        check_interval = (1, threshold - 1)
    else:
        check_interval = (threshold + 1, 4000)

    overlap = get_interval_overlap(new_xmas[letter], check_interval)
    if not overlap:
        return None
    # print(overlap)
    new_xmas[letter] = overlap

    return new_xmas


def get_otherwise_interval(xmas, conditions):
    new_xmas = xmas.copy()
    for letter, ineq, threshold, _ in conditions:
        # invert inequality
        if ineq == 1:
            check_interval = (1, threshold - 1)
        else:
            check_interval = (threshold + 1, 4000)

        overlap = get_interval_overlap(new_xmas[letter], check_interval)
        if not overlap:
            return None
        new_xmas[letter] = overlap

    return new_xmas


def get_interval_overlap(i1, i2):
    s = max(i1[0], i2[0])
    e = min(i1[1], i2[1])

    if s > e:
        return None

    return (s, e)


def sum_non_overlapping_terminals(xmas, xmases):
    """
    updates xmas to be non-overlapping with xmas2
    if xmas is a subset of xmas2, return None
    """
    pass


def solution(inp):
    workflows = {}  # {workflow: List[Tuple]}

    for i, line in enumerate(inp):
        if line == "":
            raw_workflow = inp[:i]

    # Encode < as 0, > as 1, each logic is a tuple i.e. (letter, 0, 35, dest) -> <35:dest
    # for the else condition we'll do {e: dest}
    for line in raw_workflow:
        matches = regex.match(r"(.+)\{(.+)\}", line)
        name = matches.group(1)
        checks = matches.group(2).split(",")
        conditions = []
        for check in checks[:-1]:
            condition, destination = check.split(":")
            matches = regex.match(r"(.+)([<>])(.+)", condition)
            letter, ineq, threshold = (
                matches.group(1),
                matches.group(2),
                matches.group(3),
            )
            conditions.append((letter, int(ineq == ">"), int(threshold), destination))
        workflows[name] = Node(set(), conditions, checks[-1])

    curr = set()
    # Another loop to build the graph, pointing each node to their parents
    for parent, node in workflows.items():
        for condition in node.conditions + [(-1, -1, -1, node.otherwise)]:
            child = condition[3]
            if child == "R":
                pass
            elif child == "A":
                curr.add(parent)
            else:
                workflows[child].parents.add(parent)

    workflows["in"].parents.add("seed")
    print("built tree")

    # dfs
    default_xmas = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
    all_xmas = []

    def dfs(xmas, node_name) -> None:
        if node_name == "seed":
            all_xmas.append(xmas)
            return
        workflow = workflows[node_name]
        conditions, parents = (workflow.conditions, workflow.parents)
        for condition in conditions:
            new_xmas = update_xmas(xmas, condition)
            if new_xmas:
                for parent in parents:
                    dfs(new_xmas, parent)

        # parse the otherwise condition
        otherwise_interval = get_otherwise_interval(xmas, conditions)
        if otherwise_interval:
            for parent in parents:
                dfs(otherwise_interval, parent)

    for parent in curr:
        dfs(default_xmas.copy(), parent)

    print("found all leaf intervals")

    final_xmas = {
        "x": (9999, -9999),
        "m": (9999, -9999),
        "a": (9999, -9999),
        "s": (9999, -9999),
    }
    for xmas in all_xmas:
        for letter, interval in final_xmas.items():
            low = min(xmas[letter][0], interval[0])
            high = max(xmas[letter][1], interval[1])
            final_xmas[letter] = (low, high)
    
    for xmas in all_xmas[:10]:
        print(xmas)
    print(final_xmas)
    # two intervals can only be split if one is a subset of another

    # If we let internal volume of theses cubes be V,
    # Finding V' = 4000^4 - V is actually just a O(n) process

    # but still need a way to find intersect of 4D hypercubes


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
