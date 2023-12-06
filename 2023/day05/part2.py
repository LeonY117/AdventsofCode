def solution(input):
    seed = [int(s) for s in input[0].split(": ")[1].split(" ")]
    curr = {}
    for i in range(0, len(seed), 2):
        s, e = seed[i], seed[i] + seed[i + 1]
        # key: tuple of source (s, e),
        # value: target interval (l, r), default to itself
        curr[(s, e)] = (s, e)

    for i in range(1, len(input)):
        line = input[i]
        # for a new phase, swap value to be new keys
        if not line[0].isdecimal():
            curr = {v: v for v in curr.values()}
            continue
        v, k, length = [int(n) for n in line.split(" ")]
        add = {}
        remove = []
        for s, e in curr.keys():
            # [l, r] is the overlapped region
            l, r = max(s, k), min(e, k + length)
            # if there exists a overlap of intervals, stage the following changes:
            if r > l:
                # 1) remove original interval
                remove.append((s, e))
                # 2) add overlapped interval with its destination values
                add[(l, r)] = (v + (l - k), v + (r - k))
                # 3) add non-overlapped intervals that map to itself
                if s < l:
                    add[(s, l)] = (s, l)
                if r < e:
                    add[(r, e)] = (r, e)
        # make staged changes
        for key in remove:
            curr.pop(key)
        curr.update(add)

    out = min(v[0] for v in curr.values())
    return out


if __name__ == "__main__":
    with open("fin_input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines() if l != "\n"]

    print(solution(lines))  # 7873084, for fin's input: 60294664
