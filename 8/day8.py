def readInput(day):
    with open(str(day) + r"\input.txt","r") as f:
        input = [l.strip() for l in f.read().split("\n")]
    return input

def findLoop(input):
    acc = 0
    visited = list()
    curr = 0

    while curr < len(input):
        if(curr in visited):
            return (True, acc)
        cmd, param = input[curr].split(" ")
        visited.append(curr)

        if(cmd == "acc"):
            acc += int(param)       
        elif(cmd == "jmp"):
            curr += int(param)
            continue
        curr += 1
    return (False, acc)

def part1(input):
    return findLoop(input)[1]

def part2(input):
    for i in range(len(input)):
        cmd = input[i].split(" ")[0]

        if(cmd == "jmp"):
            temp = input.copy()
            temp[i] = "nop 0"
            loopFound, acc = findLoop(temp)
            if(not loopFound):
                return acc

input = readInput(8)
print("Lösung von Part 1: {}".format(part1(input.copy())))
print("Lösung von Part 2: {}".format(part2(input.copy())))