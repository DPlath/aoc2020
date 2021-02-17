import re

input = []

with open(r"6\input.txt","r") as f:
    input = [l.strip().split("\n") for l in f.read().split("\n\n")]

sum = 0

for persons in input:
    answers = set()

    for person in persons:
        for char in person:
            answers.add(char)

    sum += len(answers)

print(sum)



