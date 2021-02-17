from collections import Counter

def readInput(day):
    with open(str(day) + r"\input.txt", "r") as f:
        input = [int(l.strip()) for l in f.read().split("\n")]
    return input

def part1(input):
    input.append(0)
    input.sort()
    input.append(input[-1] + 3)

    differences = Counter()

    for i in range(len(input) - 1):
        differences[input[i+1]-input[i]] += 1

    return differences[1] * differences[3]


def part2(input):
    input.append(-3)
    input.append(0)
    input.sort()
    input.append(input[-1] + 3)
    pastValues = [0,1,1]

    for i in range(3, len(input)):
        if(input[i] - input[i-1] == 3 or input[i-1] - input[i-2] == 3):
            pastValues.append(pastValues[i-1])
        elif(input[i-2] - input[i-3] == 3 or input[i-3] - input[i-4] == 3):
            pastValues.append(pastValues[i-1] * 2)
        elif(input[i-4] - input[i-5] == 3):
            pastValues.append(pastValues[i-3] * 7)

    return pastValues[-1]

input = readInput(10)
print("Lösung von Part 1: {}".format(part1(input.copy())))
print("Lösung von Part 2: {}".format(part2(input.copy())))
