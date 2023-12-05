def solution(input):
    seeds = [int(s) for s in input[0].split(": ")[1].split(" ")]
    mapping = {a: a for a in seeds}
    for i in range(1, len(input)):
        line = input[i]
        if not line[0].isdigit():
            # make the values the new keys
            mapping = {a: a for a in mapping.values()}
        else:
            # we are assuming that there are no duplicate maps
            v, k, r = [int(n) for n in line.split(" ")]
            for source in mapping.keys():
                if k <= source < k + r:
                    mapping[source] = v + (source - k)

    return min(mapping.values())


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines() if l != "\n"]

    print(solution(lines))  # 579439039
