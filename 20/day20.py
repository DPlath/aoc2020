import re
import numpy as np
from copy import deepcopy
from functools import reduce
from math import isqrt


def readInput(day):
    with open(str(day) + r"\input.txt", "r") as f:
        input = [l.strip() for l in f.read().split("\n\n")]
    return input


def rotate(tile, times=1):
    return np.rot90(tile, times, (1, 0))


def flip(tile):
    return np.fliplr(tile)


def hasBorderAMatch(border, ownID, tiles):
    for tile in tiles:
        if(tile == ownID):
            continue

        for perm in tiles[tile]:
            check = [
                (leftBorder(perm) == border).all(),
                (rightBorder(perm) == border).all(),
                (topBorder(perm) == border).all(),
                (bottomBorder(perm) == border).all()
            ]

            if(any(check)):
                return True
    return False


def leftBorder(tile):
    return tile[:, 0]


def rightBorder(tile):
    return tile[:, len(tile[0]) - 1]


def topBorder(tile):
    return tile[0, :]


def bottomBorder(tile):
    return tile[len(tile) - 1, :]


uniqueMapping = {}


def uniqueBorders(tiles, toCheck):
    global uniqueMapping
    if(toCheck in uniqueMapping):
        return uniqueMapping[toCheck]

    unique = []
    t = tiles[toCheck]
    toSearch = [t[0], t[4]]

    for perm in toSearch:
        sides = ""
        if(not hasBorderAMatch(leftBorder(perm), toCheck, tiles)):
            sides += "L"
        if(not hasBorderAMatch(rightBorder(perm), toCheck, tiles)):
            sides += "R"
        if(not hasBorderAMatch(topBorder(perm), toCheck, tiles)):
            sides += "T"
        if(not hasBorderAMatch(bottomBorder(perm), toCheck, tiles)):
            sides += "B"

        if(sides):
            unique.append((sides, perm))

    uniqueMapping[toCheck] = unique
    return unique


def rotateTo(tile, target, current):
    if(len(target) == 1):
        while current != target:
            if(current == "L"):
                tile = rotate(tile)
                current = "T"
            elif(current == "T"):
                tile = rotate(tile)
                current = "R"
            elif(current == "R"):
                tile = rotate(tile)
                current = "B"
            elif(current == "B"):
                tile = rotate(tile)
                current = "L"
    else:
        while current != target:
            if(current == "LB"):
                tile = rotate(tile)
                current = "LT"
            elif(current == "LT"):
                tile = rotate(tile)
                current = "RT"
            elif(current == "RT"):
                tile = rotate(tile)
                current = "RB"
            elif(current == "RB"):
                tile = rotate(tile)
                current = "LB"
    return tile


def placeTile(tiles, imageIndices, finalTiles, row, column, numberOfUniques=0, uniqueDirection=""):
    size = isqrt(len(tiles))
    for t in tiles:
        if(t in imageIndices):
            continue

        if(numberOfUniques):
            uniqueB = uniqueBorders(tiles, t)

            if(uniqueB):
                if(len(uniqueB[0][0]) == numberOfUniques):
                    for j in range(len(uniqueB)):
                        current = rotateTo(
                            uniqueB[j][1], uniqueDirection, uniqueB[j][0])
                        place = False

                        if(not row):
                            if((leftBorder(current) == rightBorder(finalTiles[imageIndices[0, column-1]])).all()):
                                place = True
                        elif(row and not column):
                            if((topBorder(current) == bottomBorder(finalTiles[imageIndices[row-1, column]])).all()):
                                place = True
                        else:
                            if((leftBorder(current) == rightBorder(finalTiles[imageIndices[row, column-1]])).all()):
                                if((topBorder(current) == bottomBorder(finalTiles[imageIndices[row-1, column]])).all()):
                                    place = True

                        if(place):
                            imageIndices[row, column] = t
                            finalTiles[t] = current
                            return
        else:
            for perm in tiles[t]:
                if((leftBorder(perm) == rightBorder(finalTiles[imageIndices[row, column-1]])).all()):
                    if((topBorder(perm) == bottomBorder(finalTiles[imageIndices[row-1, column]])).all()):
                        imageIndices[row, column] = t
                        finalTiles[t] = perm
                        return


def orderIndices(tiles):
    size = isqrt(len(tiles))
    imageIndices = np.zeros(((size,)*2))
    finalTiles = deepcopy(tiles)

    # Find first corner
    for t in tiles:
        unique = uniqueBorders(tiles, t)

        if(unique):
            if(len(unique[0][0]) == 2):
                current = rotateTo(unique[1][1], "LT", unique[1][0])
                imageIndices[0, 0] = t
                finalTiles[t] = current
                break

    # Top Row
    for i in range(1, size-1):
        placeTile(tiles, imageIndices, finalTiles, 0, i, 1, "T")

    # Top Right Corner
    placeTile(tiles, imageIndices, finalTiles, 0, size-1, 2, "RT")

    # Middle Left
    for i in range(1, size-1):
        placeTile(tiles, imageIndices, finalTiles, i, 0, 1, "L")

    # Fill all but Final Row
    for row in range(1, size-1):
        for column in range(1, size-1):
            placeTile(tiles, imageIndices, finalTiles, row, column)

    # Middle Right
    for i in range(1, size-1):
        placeTile(tiles, imageIndices, finalTiles, i, size-1, 1, "R")

    # Final Row
    placeTile(tiles, imageIndices, finalTiles, size-1, 0, 2, "LB")

    for i in range(1, size-1):
        placeTile(tiles, imageIndices, finalTiles, size-1, i, 1, "B")

    placeTile(tiles, imageIndices, finalTiles, size-1, size-1, 2, "RB")

    return imageIndices, finalTiles


def removeBorderOfTile(tile):
    return tile[1:-1, 1:-1]


def assembleImage(indices, tiles):
    size = isqrt(len(tiles))
    for t in tiles:
        tiles[t] = removeBorderOfTile(tiles[t])

    rows = []

    for row in indices:
        arrayTuple = tuple([tiles[t] for t in row])
        rows.append(np.concatenate(arrayTuple, axis=1))

    return np.concatenate(tuple(rows))


def parseInput(input):
    allTiles = {}

    for tile in input:
        lines = tile.split("\n")
        id = int(re.findall("Tile (\d+):", lines[0])[0])

        lines = lines[1:]
        grid = np.zeros((len(lines), len(lines[0])))

        for y, value in enumerate(lines):
            for x in range(len(value)):
                if(value[x] == "#"):
                    grid[y, x] = 1

        allPermutations = [grid]
        for i in range(1, 4):
            allPermutations.append(rotate(grid, i))
        allPermutations.append(flip(grid))
        for i in range(1, 4):
            allPermutations.append(rotate(flip(grid), i))

        allTiles[id] = allPermutations

    return allTiles


def numberOfSeaMonsters(image):
    #                      #
    #    #    ##    ##    ###
    #     #  #  #  #  #  #

    count = 0

    for y in range(len(image[0])-2):
        for x in range(len(image[0])-19):
            seaMonster = [
                image[y, x+18] == 1,
                image[y+1, x] == 1,
                image[y+1, x+5] == 1,
                image[y+1, x+6] == 1,
                image[y+1, x+11] == 1,
                image[y+1, x+12] == 1,
                image[y+1, x+17] == 1,
                image[y+1, x+18] == 1,
                image[y+1, x+19] == 1,
                image[y+2, x+1] == 1,
                image[y+2, x+4] == 1,
                image[y+2, x+7] == 1,
                image[y+2, x+10] == 1,
                image[y+2, x+13] == 1,
                image[y+2, x+16] == 1
            ]

            if(all(seaMonster)):
                count += 1

    return count


def part1(tiles):
    cornerIds = []

    for t in tiles:
        unique = uniqueBorders(tiles, t)

        if(unique):
            if(len(unique[0][0]) == 2):
                cornerIds.append(t)

    return int(reduce(lambda x, y: x*y, cornerIds, 1))


def part2(tiles):
    indices, finalTiles = orderIndices(tiles)
    finalImage = assembleImage(indices, finalTiles)

    # Build all Permutations of Image
    allPermutations = [finalImage]
    for i in range(1, 4):
        allPermutations.append(rotate(finalImage, i))
    allPermutations.append(flip(finalImage))
    for i in range(1, 4):
        allPermutations.append(rotate(flip(finalImage), i))

    for perm in allPermutations:
        count = numberOfSeaMonsters(perm)
        if(count > 0):
            return int(np.sum(perm) - count * 15)


input = readInput(20)
tiles = parseInput(input)

print("Lösung von Part 1: {}".format(part1(deepcopy(tiles))))
print("Lösung von Part 2: {}".format(part2(deepcopy(tiles))))
