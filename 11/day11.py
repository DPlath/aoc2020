from copy import deepcopy


def readInput(day):
    with open(str(day) + r"\input.txt", "r") as f:
        input = [l.strip() for l in f.read().split("\n")]

        for i in range(len(input)):
            input[i] = [char for char in input[i]]
    return input


def getNumberOfAdjacent(input, x, y):
    adjacent = []

    for yInc in [-1, 0, 1]:
        for xInc in [-1, 0, 1]:
            if(not (yInc == 0 and xInc == 0)):
                xTemp = x + xInc
                yTemp = y + yInc

                if(yTemp in range(len(input)) and xTemp in range(len(input[yTemp]))):
                    adjacent.append(input[yTemp][xTemp] == "#")

    return sum(adjacent)


def getNumberOfVisible(input, x, y):
    visible = []

    for yInc in [-1, 0, 1]:
        for xInc in [-1, 0, 1]:
            if(not (yInc == 0 and xInc == 0)):
                xTemp = x + xInc
                yTemp = y + yInc

                while yTemp in range(len(input)) and xTemp in range(len(input[yTemp])) and input[yTemp][xTemp] == ".":
                    xTemp = xTemp + xInc
                    yTemp = yTemp + yInc

                if(yTemp in range(len(input)) and xTemp in range(len(input[yTemp]))):
                    visible.append(input[yTemp][xTemp] == "#")

    return sum(visible)


def seatingRound(input, function, condition):
    changed = False
    newState = deepcopy(input)

    for y in range(len(input)):
        for x in range(len(input[y])):
            if(input[y][x] == "L" and function(input, x, y) == 0):
                newState[y][x] = "#"
                changed = True
            elif(input[y][x] == "#" and function(input, x, y) >= condition):
                newState[y][x] = "L"
                changed = True

    if(changed):
        input = deepcopy(newState)

    return input, changed


def part1(input):
    changed = True

    while(changed):
        input, changed = seatingRound(input, getNumberOfAdjacent, 4)

    ctr = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if(input[y][x] == "#"):
                ctr += 1

    return ctr


def part2(input):
    changed = True

    while(changed):
        input, changed = seatingRound(input, getNumberOfVisible, 5)

    ctr = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if(input[y][x] == "#"):
                ctr += 1

    return ctr


input = readInput(11)
print("Lösung von Part 1: {}".format(part1(input.copy())))
print("Lösung von Part 2: {}".format(part2(input.copy())))
