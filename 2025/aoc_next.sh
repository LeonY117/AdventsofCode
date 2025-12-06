#!/usr/bin/env bash

# config
year="2025"
max_day=0

echo "Checking through folders from previous days..."

for dir in day*/; do
    if [ ! -d "$dir" ]; then
        echo "No day directories found" 1>&2
        break
    fi
    # Remove /
    dir="${dir%/}"
    # Remove day
    number="${dir#day}"
    # Convert to number in base 10
    number=$((10#$number))

    if [ "$number" -gt "$max_day" ]; then
        max_day="$number"
    fi
done

day="$((max_day+1))"
DD="$(printf "%02d" "$day")"

echo "Creating directory './day$DD'..."
dir="day$DD"
mkdir $dir
echo "Created ./day$DD"

echo "Fetching todays input to ./day${DD}/input.txt..."

if aocd 2025 "$day" > "day${DD}/input.txt"; then
    echo "Fetched today's input!"
else
    echo "Something went wrong with fetching input, make sure you have stored the cookie."
    echo "(or maybe you are too impatient)?"
fi
echo ""

echo "Generating Python boilerplate files"

nl=$'\\n'
read -r -d '' boilerplate <<-EOF
from utils import *

def solution(inp):
    pass

if __name__ == "__main__":
    lines = get_input_for_day($day)
    # lines = get_file_for_day($day, "test_input")
    print(solution(lines))

EOF

FILE1="./day$DD/part1.py"
FILE2="./day$DD/part2.py"

echo "Creating '$FILE1' with boilerplate"
echo "$boilerplate" > "$FILE1"
echo "Creating '$FILE2' with boilerplate"
echo "$boilerplate" > "$FILE2"
touch "./day$DD/__init__.py"

# Set executable permissions.
chmod +x "$FILE1"
chmod +x "$FILE2"

echo "Opening in VS Code..."
code "./day$DD/input.txt"
code "./day$DD/part1.py"
code "./day$DD/part2.py"
cd "./day$DD"
echo ""

echo "Opening today's challenge in browser...."
echo "https://adventofcode.com/$year/day/$day"
open "https://adventofcode.com/$year/day/$day"
echo ""

echo "Done!"
echo ""
echo "======================================"