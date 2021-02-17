from collections import deque

def readInput(day):
    with open(str(day) + r"\input.txt", "r") as f:
        input = [l.strip() for l in f.read().split("\n")]
    return input

def evalMathPartOne(math):
    # Schritt 1: Klammern suchen
    while("(" in math):
        indexOpening = math.find("(")
        bracketDepth = 1
        for i in range(indexOpening + 1, len(math)):
            if(math[i] == "("):
                bracketDepth += 1
            if(math[i] == ")"):
                bracketDepth -= 1
                if(not bracketDepth):
                    res = evalMathPartOne(math[indexOpening+1:i])
                    math = math[:indexOpening] + str(res) + math[i+1:]
                    break


    # Schritt 2: Wenn keine Klammern in Ausdruck => Stück für Stück auswerten
    stack = deque()
    for i in reversed(math.split()):
        stack.append(i)

    while len(stack) > 1:
        first = stack.pop()
        op = stack.pop()
        second = stack.pop()
        stack.append(str(eval(first + op + second))) 

    return int(stack.pop())

def evalMathPartTwo(math):
    # Schritt 1: Klammern suchen
    while("(" in math):
        indexOpening = math.find("(")
        bracketDepth = 1
        for i in range(indexOpening + 1, len(math)):
            if(math[i] == "("):
                bracketDepth += 1
            if(math[i] == ")"):
                bracketDepth -= 1
                if(not bracketDepth):
                    res = evalMathPartTwo(math[indexOpening+1:i])
                    math = math[:indexOpening] + str(res) + math[i+1:]
                    break

    # Schritt 2: Plus vor Mal
    while("+" in math):
        split = math.split()
        indexPlus = next(i for i, v in enumerate(split) if v == "+")
        toCompute = " ".join(split[indexPlus-1:indexPlus+2])
        res = str(eval(toCompute))
        math = math.replace(toCompute, res, 1)

    # Schritt 3: Wenn keine Klammern und kein + mehr in Ausdruck => Stück für Stück auswerten
    stack = deque()
    for i in reversed(math.split()):
        stack.append(i)

    while len(stack) > 1:
        first = stack.pop()
        op = stack.pop()
        second = stack.pop()
        stack.append(str(eval(first + op + second))) 

    return int(stack.pop())    

def part1(input):
    sum = 0
    for math in input:
        sum += evalMathPartOne(math)
    return sum

def part2(input):
    sum = 0
    for math in input:
        sum += evalMathPartTwo(math)

    return sum


input = readInput(18)

print("Lösung von Part 1: {}".format(part1(input.copy())))
print("Lösung von Part 2: {}".format(part2(input.copy())))
