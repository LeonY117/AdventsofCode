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
    inp = get_input_for_day($day)
    # inp = get_file_for_day($day, "test_input")
    print(solution(inp))

EOF

FILE1="./day$DD/part1.py"
if [ -f "$FILE1" ]; then
    echo "$FILE1 already exists, skipping."
else
    echo "Creating '$FILE1' with boilerplate"
    echo "$boilerplate" > "$FILE1"
fi
FILE2="./day$DD/part2.py"
if [ -f "$FILE2" ]; then
    echo "$FILE2 already exists, skipping."
else
    echo "Creating '$FILE2' with boilerplate"
    echo "$boilerplate" > "$FILE2"
fi
chmod +x "$FILE1"
chmod +x "$FILE2"
echo "(Set executable permissions)"
echo ""
touch "./day$DD/__init__.py"

echo "Opening in VS Code..."
code "./day$DD/input.txt"
code "./day$DD/part1.py"
code "./day$DD/part2.py"
cd "./day$DD"
echo ""

number_no_leading=$(echo $DD | sed 's/^0*//')
echo "Opening today's challenge in browser...."
echo "https://adventofcode.com/$year/day/$number_no_leading"
open "https://adventofcode.com/$year/day/$number_no_leading"
echo ""

echo "Done!"
echo ""
echo "======================================"