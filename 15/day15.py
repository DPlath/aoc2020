import re
import itertools
from functools import reduce


def readInput(day):
    with open(str(day) + r"\input.txt", "r") as f:
        input = [int(l.strip()) for l in f.read().split(",")]
    return input


def runGame(input, limit):
    last = input[-1]
    ages = {v: i + 1 for i, v in enumerate(input)}

    length = len(input)
    while length < limit:
        if(last not in ages):
            ages[last] = length
            last = 0
            length += 1
        else:
            ageDifference = length - ages[last]
            ages[last] = length
            last = ageDifference
            length += 1

    return last


def part1(input):
    return runGame(input, 2020)


def part2(input):
    return runGame(input, 30000000)


input = readInput(15)

print("Lösung von Part 1: {}".format(part1(input.copy())))
print("Lösung von Part 2: {}".format(part2(input.copy())))
