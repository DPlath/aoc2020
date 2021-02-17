import re

input = []

with open(r"7\input.txt","r") as f:
    input = [l.strip() for l in f.read().split("\n")]

bags = dict()

def canContain(bag, toSearch):
    content = bags[bag] 
    if(len(content) == 0):
        return False

    if(toSearch in content):
        return True

    subSearch = []
    for subBag in content:
        subSearch.append(canContain(subBag,toSearch))

    return any(subSearch)

for rule in input:
    bag, bagRule = rule.split("contain")
    bag = bag.split("bags")[0].rstrip()
    bagRule = bagRule[:-1].lstrip()

    if("no other bags" in bagRule):
        bags[bag] = dict()
        continue

    bags[bag] = dict()
    splitRules = [r.strip() for r in bagRule.split(",")]

    for r in splitRules:
        bags[bag][r[2:-4].strip()] = r[:2]

ctr = 0
for bag in bags:
    if(canContain(bag, "shiny gold")):
        ctr += 1

print(ctr)