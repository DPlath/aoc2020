from functools import reduce

input = []

with open(r"3\input.txt","r") as f:
    for s in f:
        input.append(s.rstrip())

def countTreesForSlope(xInc, yInc):
    trees = 0
    x = 0
    y = 0
    while (y + yInc) < len(input):
        # Slide down
        x += xInc
        y += yInc

        position = input[y][x % len(input[y])]

        if(position == "#"):
            trees += 1
    
    return trees

treeCount = [countTreesForSlope(1, 1),countTreesForSlope(3, 1),
             countTreesForSlope(5, 1),countTreesForSlope(7, 1),
             countTreesForSlope(1, 2)]

print(reduce(lambda x,y: x*y, treeCount, 1))