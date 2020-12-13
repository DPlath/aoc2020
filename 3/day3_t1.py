input = []

with open(r"3\input.txt","r") as f:
    for s in f:
        input.append(s.rstrip())#.split())

trees = 0
x = 0
y = 0
while y < len(input) - 1:
    # Slide down
    x += 3
    y += 1

    position = input[y][x % len(input[y])]

    if(position == "#"):
        trees += 1
        input[y] = input[y][:x % len(input[y])] + "X" + input[y][x % len(input[y])+1:]
    else:
        input[y] = input[y][:x % len(input[y])] + "O" + input[y][x % len(input[y])+1:]

print(trees)
