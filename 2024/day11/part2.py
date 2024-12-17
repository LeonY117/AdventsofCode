def solution(inp):
    curr = [int(n) for n in inp[0].split(" ")]
    for _ in range(20):
        next = []
        for n in curr:
            if n == 0:
                next.append(1)
            elif len(str(n)) % 2 == 0:
                n_str = str(n)
                next.append(int(n_str[:len(n_str) // 2]))
                next.append(int(n_str[len(n_str) // 2:]))
            else:
                next.append(n * 2024)
        
        curr = next

    print(curr)
    print(len(set(curr)))
    return len(curr)

if __name__ == "__main__":
    with open("test_input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
    
    print(solution(lines))
