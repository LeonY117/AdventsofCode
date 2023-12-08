def solution(input):
    instructions = list(input[0])
    # store everything into a dictionary
    network = {}
    for i in range(2, len(input)):
        line = input[i]
        key, value = line[0:3], (line[7:10], line[12:15])
        network[key] = value

    steps = 0
    curr = 'AAA'
    while curr != 'ZZZ':
        dir = instructions.pop(0)
        curr = network[curr][0] if dir == 'L' else network[curr][1]
        steps += 1
        instructions.append(dir)
    
    return steps

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
