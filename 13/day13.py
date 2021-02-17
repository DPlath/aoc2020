from sympy.ntheory.modular import solve_congruence


def readInput(day):
    with open(str(day) + r"\input.txt", "r") as f:
        input = [l.strip() for l in f.read().split("\n")]
        input = [int(input[0]), input[1].split(",")]
    return input


def crt(idsAndOffsets):
    N = 1
    for i, _ in idsAndOffsets:
        N = N * i

    key = 0
    for i, o in idsAndOffsets:
        product = N // i
        inverse = pow(product, -1, i)
        key += o * product * inverse

    return key % N


def part1(input):
    input[1] = [int(i) for i in input[1] if i != "x"]
    startTime = input[0]
    waitTime = 0

    while(True):
        for busId in input[1]:
            if((startTime + waitTime) % busId == 0):
                return waitTime * busId
        waitTime += 1


def part2(input):
    idsAndOffsets = [
        (int(v), int(v) - i)
        for i, v in enumerate(input[1])
        if v != "x"
    ]

    return crt(idsAndOffsets)

input = readInput(13)
print("Lösung von Part 1: {}".format(part1(input.copy())))
print("Lösung von Part 2: {}".format(part2(input.copy())))
