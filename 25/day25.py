from sympy import primefactors
from sympy.ntheory.modular import crt, solve_congruence
from sympy.ntheory.residue_ntheory import discrete_log

def readInput(day):
    with open(str(day) + r"\input.txt", "r") as f:
        input = [l.strip() for l in f.read().split("\n")]
    return input

subjectNumber = 7
p = 20201227

def transformSubjectNumber(subjectNumber, loopSize):
    return pow(subjectNumber, loopSize, p)

def part1(keys):
    pubKDoor = int(keys[0])
    pubKCard = int(keys[1])

    # Polard Rho
    key = discrete_log(p, pubKDoor, subjectNumber)
    
    # Brute Force
    # key = 0
    # while(transformSubjectNumber(subjectNumber, key) != pubKDoor):
    #     key += 1

    return transformSubjectNumber(pubKCard, key)

def part2():
    return "YOU FUCKIN DID IT!"

keys = readInput(25)
print("Lösung von Part 1: {}".format(part1(keys)))
print("Lösung von Part 2: {}".format(part2()))