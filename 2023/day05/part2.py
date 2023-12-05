def solution(input):
    seed = [int(s) for s in input[0].split(": ")[1].split(" ")]
    curr = {}
    for i in range(0, len(seed), 2):
        s, e = seed[i], seed[i] + seed[i + 1]
        # each key is a tuple (start, end),
        # value is the intervals that it maps to, default to itself
        curr[(s, e)] = [(s, e)]

    for i in range(1, len(input)):
        line = input[i]
        if not line[0].isdigit():
            # make the values the new keys
            curr = {v: [v] for vs in curr.values() for v in vs}
        else:
            v, k, length = [int(n) for n in line.split(" ")]
            for s, e in curr.keys():
                l = max(s, k)
                r = min(e, k + length)
                # only updates if there's overlap interval [l, r]
                if r > l:  # has to be strictly greater
                    # overwrites the default self-mapping
                    curr[(s, e)] = [(v + (l - k), v + (r - k))]
                    # map non-overlapping region(s) to self
                    if s < l:
                        curr[(s, e)].append((s, l))
                    if r < e:
                        curr[(s, e)].append((r, e))
    out = min(min(v[0] for v in vs) for vs in curr.values())
    return out


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines() if l != "\n"]

    print(solution(lines))  # 7873084
