def solution(inp):
    total = 0
    counts = [inp[0]]
    spaces = []
    # one pass so that we know the value of the counts
    for i in range(0, len(inp)-1, 2):
        count, space = inp[i], inp[i+1]
        counts.append(count)
        spaces.append(space)
    
    print(counts, spaces)

if __name__ == "__main__":
    with open("test_input.txt", "r") as f:
        line = f.readlines()[0].strip()
    
    print(solution(line))
