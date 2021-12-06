with open('input.txt') as f:
    commands = f.readlines()
    for (i, c) in enumerate(commands):
        commands[i] = (c.split(' ')[0], int(c.split(' ')[1]))

depth = 0
distance = 0

for c in commands:
    if c[0] == 'up':
        depth -= c[1]
    if c[0] == 'down':
        depth += c[1]
    if c[0] == 'forward':
        distance += c[1]

# print(distance * depth)


# Part 2

depth = 0
distance = 0
aim = 0
for c in commands:
    if c[0] == 'up':
        aim -= c[1]
    if c[0] == 'down':
        aim += c[1]
    if c[0] == 'forward':
        distance += c[1]
        depth += aim * c[1]
    
print(distance * depth)