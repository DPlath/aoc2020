import numpy as np

dimension = 20
pockedDimension3D = np.zeros(((dimension,)*3))
pockedDimension4D = np.zeros(((dimension,)*4))


def readInput(day):
    with open(str(day) + r"\input.txt", "r") as f:
        input = [l.strip() for l in f.read().split("\n")]
    return input


def parseInput(input, pockedDimension, dim = 3):
    height = len(input)
    width = len(input[0])
    z = dimension // 2
    w = z

    startingRow = dimension // 2 - height // 2
    startingColumn = dimension // 2 - width // 2

    for y, value in enumerate(input):
        for x in range(len(value)):
            if(value[x] == "#"):
                if(dim == 3):
                    pockedDimension[z, startingRow + y, startingColumn + x] = 1
                else:
                    pockedDimension[w, z, startingRow + y, startingColumn + x] = 1


def numberOfNeighbors3D(pockedDimension, coord, dim = 3):
    # includes self!
    # coord (z,x,y)
    if(dim == 3):
        z, y, x = coord[0], coord[1], coord[2]
        neighborSlice = np.array(
            pockedDimension[z - 1: z + 2, y - 1: y + 2, x - 1: x + 2]
        )
    else:
        w, z, y, x = coord[0], coord[1], coord[2], coord[3]
        neighborSlice = np.array(
            pockedDimension[w - 1: w + 2, z - 1: z + 2, y - 1: y + 2, x - 1: x + 2]
        )
    return int(np.sum(neighborSlice))


def runCycle(pockedDimension, dim = 3):
    reference = np.copy(pockedDimension)

    for indices, value in np.ndenumerate(reference):
        if(value == 1):
            neighbors = numberOfNeighbors3D(reference, indices, dim) - 1
            if(neighbors not in range(2, 4)):
                pockedDimension[indices] = 0
        else:
            neighbors = numberOfNeighbors3D(reference, indices, dim)
            if(neighbors == 3):
                pockedDimension[indices] = 1

    return pockedDimension


def part1(pockedDimension):
    for _ in range(6):
        runCycle(pockedDimension)

    return int(np.sum(pockedDimension))


def part2(pockedDimension):
    for _ in range(6):
        runCycle(pockedDimension, 4)
        
    return int(np.sum(pockedDimension))


input = readInput(17)
parseInput(input, pockedDimension3D)
parseInput(input, pockedDimension4D, 4)

print("Lösung von Part 1: {}".format(part1(np.copy(pockedDimension3D))))
print("Lösung von Part 2: {}".format(part2(np.copy(pockedDimension4D))))
