class Cup:
    def __init__(self, value):
        self.nextCup = None
        self.value = value


class Circle:
    cups = {}
    head = None
    tail = None
    biggestValue = 0

    def addCup(self, cup):
        id = cup.value
        self.cups[id] = cup

        if(not self.head and not self.tail):
            self.head = id
            self.tail = id

        if(len(self.cups) >= 2):
            cup.nextCup = self.cups[self.head]
            self.cups[self.tail].nextCup = cup
            self.tail = id

        self.biggestValue = max(self.biggestValue, id)

    def insertCupsBehindValue(self, toInsert, value):
        self.cups[toInsert[-1].value].nextCup = self.cups[value].nextCup
        self.cups[value].nextCup = self.cups[toInsert[0].value]

def parseInput(input, part2 = False):
    c = Circle()

    for s in input:
        cup = Cup(int(s))
        c.addCup(cup)

    if(part2):
        for i in range(len(c.cups) + 1, 1000001):
            cup = Cup(i)
            c.addCup(cup)

    return c

def performMove(circle, current):
    pickedUp = [
        circle.cups[current].nextCup,
        circle.cups[current].nextCup.nextCup,
        circle.cups[current].nextCup.nextCup.nextCup
    ]

    # Remove
    circle.cups[current].nextCup = pickedUp[2].nextCup

    destinationCupValue = current - 1
    if(destinationCupValue == 0):
        destinationCupValue = circle.biggestValue

    while(destinationCupValue in [c.value for c in pickedUp]):
        destinationCupValue -= 1
        if(destinationCupValue == 0):
            destinationCupValue = circle.biggestValue

    circle.insertCupsBehindValue(pickedUp, destinationCupValue)


def part1(circle):
    current = next(iter(circle.cups.keys()))

    for _ in range(100):
        performMove(circle, current)
        current = circle.cups[current].nextCup.value

    output = ""
    one = circle.cups[1]
    curr = one.nextCup
    while(curr is not one):
        output += str(curr.value)
        curr = curr.nextCup

    return output


def part2(circle):
    current = next(iter(circle.cups.keys()))

    for i in range(10000000):
        performMove(circle, current)
        current = circle.cups[current].nextCup.value

    one = circle.cups[1]
    return one.nextCup.value * one.nextCup.nextCup.value


input = "186524973"
circleSMALL = parseInput(input)
print("Lösung von Part 1: {}".format(part1(circleSMALL)))
circleBIG = parseInput(input, part2=True)
print("Lösung von Part 2: {}".format(part2(circleBIG)))