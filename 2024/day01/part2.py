def solution(inp):
    nums, hashmap = [], {}
    for pair in inp:
        n1, n2 = pair.split()
        nums.append(n1)
        if n2 not in hashmap:
            hashmap[n2] = 0
        hashmap[n2] += 1

    total_score = 0
    for n in nums:
        total_score += int(n) * hashmap.get(n, 0)
    
    return total_score

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
    
    print(solution(lines))
