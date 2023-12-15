def solution(input):
    strings = input[0].split(",")

    def HASH(s):
        curr = 0
        for char in s:
            curr += ord(char)
            curr *= 17
            curr %= 256
        return curr

    out = 0
    for s in strings:
        out += HASH(s)

    return out


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))  # 510801
