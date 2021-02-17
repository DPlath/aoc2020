import re
import itertools
from functools import reduce


def readInput(day):
    with open(str(day) + r"\input.txt", "r") as f:
        input = [l.strip() for l in f.read().split("\n")]
    return input


def getAllMemoryIndices(index, mask):
    binaryS = bin(index)[2:].zfill(36)
    binaryL = list(binaryS)

    for i, c in enumerate(mask):
        if(c == "X"):
            binaryL[i] = c
        elif(c == "1"):
            binaryL[i] = c

    result = "".join(binaryL)
    count = result.count("X")

    indices = []
    for perm in ["".join(seq) for seq in itertools.product("01", repeat=count)]:
        tempList = list(result)

        for i, c in enumerate(result):
            if(c == "X"):
                tempList[i] = perm[0]
                perm = perm[1:]

        indices.append("".join(tempList))

    return [int(i, 2) for i in indices]


def applyMask(value, mask):
    binaryS = bin(value)[2:].zfill(36)
    binaryL = list(binaryS)

    for i, c in enumerate(mask):
        if(c != "X"):
            binaryL[i] = c

    result = "".join(binaryL)

    return int(result, 2)


def part1(input):
    currentMask = ""
    mem = dict()

    for command in input:
        if("mask" in command):
            currentMask = command.split("=")[1].strip()
        else:
            index, value = [int(i) for i in re.findall(
                r"mem\[(\d+)\] = (\d+)", command)[0]]
            mem[index] = applyMask(value, currentMask)

    return sum(mem.values())


def part2(input):
    currentMask = ""
    mem = dict()

    for command in input:
        if("mask" in command):
            currentMask = command.split("=")[1].strip()
        else:
            index, value = [int(i) for i in re.findall(
                r"mem\[(\d+)\] = (\d+)", command)[0]]
            for i in getAllMemoryIndices(index, currentMask):
                mem[i] = value

    return sum(mem.values())


input = readInput(14)
print("Lösung von Part 1: {}".format(part1(input.copy())))
print("Lösung von Part 2: {}".format(part2(input.copy())))
