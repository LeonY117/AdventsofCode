#!/usr/bin/env bash
# stole this magic from Fin: https://github.com/finwarman/advent-of-code-2023/tree/main

# config
year="2023"

# place aoc 'session' cookie into '.aoc_session'
session_file=".aoc_session"
export AOC_SESSION=$(cat "$session_file")

echo "======== Advent of Code Setup ========="
echo ""

read YYYY MM DD <<<$(date +'%Y %m %d')
echo "Today is Day $DD of Advent of Code!"
echo ""

echo "Creating directory './day$DD'..."
dir="day$DD"
if [[ ! -d $dir ]]; then
    mkdir $dir
    echo "Created ./day$DD"
else
    echo "Directory ./$dir already exists, continuing..." 1>&2
fi
echo ""

echo "Fetching todays input to ./day$DD/input.txt..."
aocd > "./day$DD/input.txt"
echo "Done!"
echo ""


echo "Generating Python boilerplate files"

nl=$'\\n'
read -r -d '' boilerplate <<-EOF
def solution(inp):
    pass

if __name__ == "__main__":
    with open("inp.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
    
    print(solution(lines))

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