def readInput(day):
    with open(str(day) + r"\input.txt", "r") as f:
        input = [int(l.strip()) for l in f.read().split("\n")]
    return input


def isValid(previousNumbers, number):
    for i in range(len(previousNumbers)):
        for j in range(i+1, len(previousNumbers)):
            if(previousNumbers[i] + previousNumbers[j] == number):
                return True
    return False


def getContigousSet(input, currentIndex, targetNum) -> list:
    result = []

    while(sum(result) < targetNum and currentIndex < len(input)):
        result.append(input[currentIndex])
        if(sum(result) == targetNum):
            return result
        currentIndex += 1

    return []


def part1(input):
    Preambel = 25

    for i in range(Preambel, len(input)):
        if(not isValid(input[i-Preambel:i], input[i])):
            return "{} bei Index {}".format(input[i], i)
    return "None found"


def part2(input):
    target = 542529149
    targetIndex = 616

    for i in range(0, targetIndex):
        result = getContigousSet(input[:targetIndex], i, target)
        if(result):
            return "{} + {} = {}".format(min(result), max(result), min(result) + max(result))
    return "None found."


input = readInput(9)
print("Lösung von Part 1: {}".format(part1(input.copy())))
print("Lösung von Part 2: {}".format(part2(input.copy())))
