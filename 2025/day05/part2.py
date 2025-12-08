from utils import *


def insert_interval(new_interval, curr_intervals):
    l, r = new_interval
    found_intersection = False
    for i, interval in enumerate(curr_intervals):
        a, b = interval
        if l <= a <= r or l <= b <= r:
            combined_interval = (min(a, l), max(b, r))
            curr_intervals[i] = combined_interval
            found_intersection = True
    if not found_intersection:
        curr_intervals.append(new_interval)


def merge_intervals_once(curr_intervals):
    merged_intervals = []
    while curr_intervals:
        interval = curr_intervals.pop()
        insert_interval(interval, merged_intervals)
    return merged_intervals


def merge_intervals(curr_intervals):
    prev_length, curr_length = 0, len(curr_intervals)
    while prev_length != curr_length:
        prev_length = curr_length
        curr_intervals = merge_intervals_once(curr_intervals)
        curr_length = len(curr_intervals)
    return curr_intervals


def solution(inp):
    # all intervals to search through
    all_intervals = [(int(lr.split("-")[0]), int(lr.split("-")[1])) for lr in inp[0]]
    valid_intervals = merge_intervals(all_intervals)
    out = sum((itv[1] - itv[0] + 1 for itv in valid_intervals))
    return out


if __name__ == "__main__":
    lines = get_input_for_day(5, split_chunks=True)
    # lines = get_file_for_day(5, "my_test", split_chunks=True)
    print(solution(lines))
