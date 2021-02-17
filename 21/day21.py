def readInput(day):
    with open(str(day) + r"\input.txt", "r") as f:
        input = [l.strip() for l in f.read().split("\n")]
    return input


def parseInput(input):
    # Result: [[ingredients],[allergens]], dict(allergens:none)
    result = []
    allAlergens = {}

    for line in input:
        foods = line.split("(")[0].split()
        allergens = [i[:-1] for i in line.split("(contains ")[1].split(" ")]
        result.append((foods, allergens))

        for a in allergens:
            allAlergens[a] = None

    return result, allAlergens


def getAllergenList(allAlergens, ingredients):
    while(None in allAlergens.values()):
        for a in allAlergens:
            items = set()

            for ingredList in ingredients:
                if(a in ingredList[1]):
                    if(len(items) == 0):
                        for f in ingredList[0]:
                            if(f not in allAlergens.values()):
                                items.add(f)
                    else:
                        intersec = set(i for i in ingredList[0])
                        items = items.intersection(intersec)

            if(len(items) == 1 and allAlergens[a] == None):
                allAlergens[a] = items.pop()


def part1(ingredients, allAlergens):
    getAllergenList(allAlergens, ingredients)

    counter = 0
    for ingredList in ingredients:
        for f in ingredList[0]:
            if f not in allAlergens.values():
                counter += 1

    return counter


def part2(allAlergens):
    sortedKeys = sorted(allAlergens.keys(), key=lambda x:x.lower())
    output = ""
    for key in sortedKeys:
        output = output + allAlergens[key] + ","
    output = output[:-1]

    return output


input = readInput(21)
ingredients, allAlergens = parseInput(input)

print("Lösung von Part 1: {}".format(part1(ingredients, allAlergens)))
print("Lösung von Part 2: {}".format(part2(allAlergens)))
