from utils import *

def prod(nums):
    out = 1
    for n in nums:
        out *= n
    return out

def solution(inp):
    all_num_rows = [[int(n) for n in line.split()] for line in inp[:-1]]
    all_nums = list(map(list, zip(*all_num_rows)))
    operations = [s for s in inp[-1].split()]
    out = 0
    for o, nums in zip(operations, all_nums): 
        if o == "+":
            out += sum(nums)
        else:
            out += prod(nums)
    return out

if __name__ == "__main__":
    # lines = get_input_for_day(6)
    lines = get_file_for_day(6, "test_input")
    print(solution(lines))
