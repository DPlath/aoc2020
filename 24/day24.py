from itertools import islice
from copy import deepcopy


class HexTile:
    def __init__(self):
        self.nw = None
        self.ne = None
        self.e = None
        self.se = None
        self.sw = None
        self.w = None
        self.side = 0
        self.debug_layer = -1

    def getNeighbors(self):
        return [
            self.nw,
            self.ne,
            self.e,
            self.se,
            self.sw,
            self.w
        ]


class Grid:
    allTiles = []

    def __init__(self, reference):
        self.reference = reference
        self.allTiles.append(reference)


def readInput(day):
    with open(str(day) + r"\input.txt", "r") as f:
        input = [l.strip() for l in f.read().split("\n")]
    return input


def buildGrid(iterations):
    ref = HexTile()
    grid = Grid(ref)

    for i in range(iterations):
        toIterate = islice(grid.allTiles, 0, len(grid.allTiles))
        for tile in toIterate:
            if(tile.nw == None):
                tile.nw = HexTile()
                tile.nw.debug_layer = i
                tile.nw.se = tile

                if(tile.w):
                    tile.nw.sw = tile.w
                    tile.w.ne = tile.nw

                if(tile.ne):
                    tile.nw.e = tile.ne
                    tile.ne.w = tile.nw

                grid.allTiles.append(tile.nw)
            if(tile.ne == None):
                tile.ne = HexTile()
                tile.ne.debug_layer = i
                tile.ne.sw = tile

                if(tile.nw):
                    tile.ne.w = tile.nw
                    tile.nw.e = tile.ne

                if(tile.e):
                    tile.ne.se = tile.e
                    tile.e.nw = tile.ne

                grid.allTiles.append(tile.ne)
            if(tile.e == None):
                tile.e = HexTile()
                tile.e.debug_layer = i
                tile.e.w = tile

                if(tile.ne):
                    tile.e.nw = tile.ne
                    tile.ne.se = tile.e

                if(tile.se):
                    tile.e.sw = tile.se
                    tile.se.ne = tile.e

                grid.allTiles.append(tile.e)
            if(tile.se == None):
                tile.se = HexTile()
                tile.se.debug_layer = i
                tile.se.nw = tile

                if(tile.sw):
                    tile.se.w = tile.sw
                    tile.sw.e = tile.se

                if(tile.e):
                    tile.se.ne = tile.e
                    tile.e.sw = tile.se

                grid.allTiles.append(tile.se)
            if(tile.sw == None):
                tile.sw = HexTile()
                tile.sw.debug_layer = i
                tile.sw.ne = tile

                if(tile.se):
                    tile.sw.e = tile.se
                    tile.se.w = tile.sw

                if(tile.w):
                    tile.sw.nw = tile.w
                    tile.w.se = tile.sw

                grid.allTiles.append(tile.sw)
            if(tile.w == None):
                tile.w = HexTile()
                tile.w.debug_layer = i
                tile.w.e = tile

                if(tile.sw):
                    tile.w.se = tile.sw
                    tile.sw.nw = tile.w

                if(tile.nw):
                    tile.w.ne = tile.nw
                    tile.nw.sw = tile.w

                grid.allTiles.append(tile.w)

    return grid


def takeStep(tile, direction):
    if(direction == "w"):
        tile = tile.w
    elif(direction == "e"):
        tile = tile.e
    elif(direction == "nw"):
        tile = tile.nw
    elif(direction == "ne"):
        tile = tile.ne
    elif(direction == "sw"):
        tile = tile.sw
    elif(direction == "se"):
        tile = tile.se

    return tile


def numberObAdjacentBlack(tile):
    neighbors = tile.getNeighbors()
    return sum([t.side for t in neighbors if t is not None])


def part1(grid, input):
    for path in input:
        i = 0
        current = grid.reference
        while i < len(path):
            direction = path[i]
            if(direction == "s" or direction == "n"):
                direction += path[i+1]
                i += 2
            else:
                i += 1

            current = takeStep(current, direction)
        current.side = (current.side + 1) % 2

    return sum([t.side for t in grid.allTiles])


def part2(grid):
    print("Day 0: {}".format(sum([t.side for t in grid.allTiles])))
    for i in range(1, 101):
        toFlip = []
        for tile in grid.allTiles:
            count = numberObAdjacentBlack(tile)
            if(tile.side == 0):
                if(count == 2):
                    toFlip.append(tile)
            else:
                if(count == 0 or count > 2):
                    toFlip.append(tile)
        for tile in toFlip:
            tile.side = (tile.side + 1) % 2
        if(i % 10 == 0):
            print("Day {}: {}".format(i, sum([t.side for t in grid.allTiles])))

    return sum([t.side for t in grid.allTiles])

input = readInput(24)
grid = buildGrid(70)
print("Lösung von Part 1: {}".format(part1(grid, input)))
print("Lösung von Part 2: {}".format(part2(grid)))
