import re


def readInput(day, part):
    with open(str(day) + r"\input_p" + str(part) + r".txt", "r") as f:
        input = [l.strip() for l in f.read().split("\n\n")]
    return input


def parseInput(input):
    rules = {}
    messages = [i.strip() for i in input[1].split("\n")]

    for rule in input[0].split("\n"):
        rules[rule.split(":")[0].strip()] = rule.split(":")[
            1].strip().replace("\"", "")

    for r in rules:
        allDigits = set(re.findall("\d+", rules[r]))
        rules[r] = " " + rules[r] + " "
        foundItself = 0
        while(len(allDigits) != 0):
            for digit in allDigits:
                if(digit == r):
                    rules[r] = re.sub(" " + digit + " ",
                                      " ( " + rules[digit] + " ) ", rules[r])
                    foundItself += 1
                    if(foundItself > 5):
                        rules[r] = re.sub(" " + digit + " ", " ", rules[r], 1)

                elif(not rules[digit].isdigit() and len(rules[digit]) == 1):
                    rules[r] = re.sub(" " + digit + " ", " " +
                                      rules[digit] + " ", rules[r])
                else:
                    rules[r] = re.sub(" " + digit + " ",
                                      " ( " + rules[digit] + " ) ", rules[r])
            allDigits = set(re.findall("\d+", rules[r]))
        rules[r] = rules[r].replace(" ", "").strip()

    return rules, messages


def part1(rules, messages):
    toCheck = rules["0"]
    sum = 0

    for m in messages:
        if(re.fullmatch(toCheck, m)):
            sum += 1

    return sum


def part2(rules, messages):
    return part1(rules, messages)


p1_input = readInput(19, 1)
p1_rules, p1_messages = parseInput(p1_input)
p2_input = readInput(19, 2)
p2_rules, p2_messages = parseInput(p2_input)


print("Lösung von Part 1: {}".format(part1(p1_rules, p1_messages)))
print("Lösung von Part 2: {}".format(part2(p2_rules, p2_messages)))
