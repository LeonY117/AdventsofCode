def get_input_for_day(day):
    with open(f"day{day:02d}/input.txt") as f:
        lines = [l.strip() for l in f.readlines()]
    return lines


def get_file_for_day(day, filename="test"):
    with open(f"day{day:02d}/{filename}.txt") as f:
        lines = [l.strip() for l in f.readlines()]
    return lines
