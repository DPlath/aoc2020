import re

input = []

with open(r"6\input.txt","r") as f:
    input = [l.strip().split("\n") for l in f.read().split("\n\n")]

sum = 0

for persons in input:
    answers = []

    for person in persons:
        p = set(char for char in person)
        answers.append(p)

    intersects = answers[0].copy()
    for s in answers[1:]:
        intersects = intersects.intersection(s)

    sum += len(intersects)

print(sum)