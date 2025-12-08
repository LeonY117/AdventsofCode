def get_input_for_day(day, split_chunks=False, strip=True):
    return get_file_for_day(
        day, filename="input", split_chunks=split_chunks, strip=strip
    )


def get_file_for_day(day, filename="test", split_chunks=False, strip=True):
    with open(f"day{day:02d}/{filename}.txt") as f:
        if not split_chunks:
            return [l.strip() if strip else l for l in f.readlines()]
        elif split_chunks:
            all_lines = f.readlines()
            chunks, curr_chunk = [], []
            for line in all_lines:
                if line == "\n":
                    chunks.append(curr_chunk)
                    curr_chunk = []
                    continue
                curr_chunk.append(line.strip() if strip else line)
            chunks.append(curr_chunk)
            return chunks
