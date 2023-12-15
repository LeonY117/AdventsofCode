import re
from collections import OrderedDict


def solution(input):
    strings = input[0].split(",")

    def HASH(s):
        curr = 0
        for char in s:
            curr += ord(char)
            curr *= 17
            curr %= 256
        return curr

    lenses = []
    for _ in range(256):
        lenses.append(OrderedDict())  # maps str->num

    for s in strings:
        s, n = re.split(r"-|=", s)
        i = HASH(s)
        s_to_n = lenses[i]
        # subtract:
        if n == "":
            if s in s_to_n:
                del s_to_n[s]
        # add
        else:
            s_to_n[s] = int(n)

    out = 0
    for i, box in enumerate(lenses):
        for j, focal in enumerate(box.values()):
            out += (i + 1) * (j + 1) * focal

    return out


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
