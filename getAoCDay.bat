[ -z "$1" ] && echo "No day supplied!" && exit 1;

mkdir $1

session=""

echo "[+] Downloading input for day $1";
curl -s -b "session=$session" "https://adventofcode.com/2020/day/$1/input" > "$1/input.txt"

echo "[+] Creating python script.";
echo "# Advent of Code 2020 Day $1
with open(r'$1\input.txt','r') as f:
    input = [l.rstrip() for l in f]

print(input)" > "$1/$1.py";

echo "[+] Done. Opening page.";
open "https://adventofcode.com/2020/day/$1";
code .;