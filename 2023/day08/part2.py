import math 

def solution(input):
    instructions = list(input[0])
    print(len(instructions))
    # store everything into a dictionary
    network = {}
    nodes = []
    for i in range(2, len(input)):
        line = input[i]
        key, value = line[0:3], (line[7:10], line[12:15])
        network[key] = value
        if key.endswith("A"):
            nodes.append(key)

    loop_lengths = []
    for node in nodes:
        curr = node
        directions = instructions.copy()
        count = 0
        while not curr.endswith("Z"):
            count += 1
            dir = directions.pop(0)
            curr = network[curr][0] if dir == "L" else network[curr][1]
            directions.append(dir)
        loop_lengths.append(count)
    return math.lcm(*loop_lengths)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
