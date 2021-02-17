import re
from functools import reduce

def readInput(day):
    with open(str(day) + r"\input.txt", "r") as f:
        input = [l.strip() for l in f.read().split("\n\n")]
    return input


def parseInput(input):
    rules = {}

    for rule in input[0].split("\n"):
        name, values = rule.split(":")
        lowOne, highOne, lowTwo, HighTwo = re.findall(
            r"^ (\d+)-(\d+) or (\d+)-(\d+)$", values)[0]
        rules[name] = [range(int(lowOne), int(highOne)+1),
                       range(int(lowTwo), int(HighTwo)+1)]

    myTicket = [int(i) for i in input[1].split("\n")[1].split(",")]

    nearbyTickets = []
    for ticket in input[2].split("\n")[1:]:
        nearbyTickets.append([int(i) for i in ticket.split(",")])

    return rules, myTicket, nearbyTickets


def inBoundsForAny(value, rules):
    for rule in rules:
        if(value in rules[rule][0] or value in rules[rule][1]):
            return True
    return False

def inBounds(value, bounds):
    if(value in bounds[0] or value in bounds[1]):
        return True
    return False


def getInvalids(rules, nearbyTickets):
    invalids = []
    checks = {}

    for ticket in nearbyTickets:
        for value in ticket:
            if(value in checks):
                if(not checks[value]):
                    invalids.append(value)
            elif(not inBoundsForAny(value, rules)):
                checks[value] = False
                invalids.append(value)
            else:
                checks[value] = True

    return invalids


def getOrderOfTickets(rules, nearbyTickets):
    possibleOrders = {}

    for pos in range(len(nearbyTickets[0])):
        for rule in rules:
            bounds = rules[rule]

            error = False
            for ticket in nearbyTickets:
                if(not inBounds(ticket[pos], bounds)):
                    error = True
                    break
            if(not error):
                possibleOrders.setdefault(rule,[]).append(pos)

    orders = {}

    while len(possibleOrders) > 0:
        temp = possibleOrders.copy()
        for pOrder in temp:
            if(len(temp[pOrder]) == 1):
                orders[pOrder] = temp[pOrder][0]
                del possibleOrders[pOrder]
                for order in possibleOrders:
                    if(temp[pOrder][0] in possibleOrders[order]):
                        possibleOrders[order].remove(temp[pOrder][0])
    
    return orders


def part1(rules, nearbyTickets):
    return sum(getInvalids(rules, nearbyTickets))


def part2(rules, nearbyTickets, myTicket):
    invalids = getInvalids(rules, nearbyTickets)
    validTickets = []

    for ticket in nearbyTickets:
        if(not any([value in invalids for value in ticket])):
            validTickets.append(ticket)

    order = getOrderOfTickets(rules, validTickets)
    departureValues = []
    for rule in rules:
        if rule.startswith("departure"):
            departureValues.append(myTicket[order[rule]])

    return reduce(lambda x,y: x*y, departureValues, 1)


input = readInput(16)
rules, myTicket, nearbyTickets = parseInput(input)
print("Lösung von Part 1: {}".format(part1(rules, nearbyTickets)))
print("Lösung von Part 2: {}".format(part2(rules, nearbyTickets, myTicket)))
