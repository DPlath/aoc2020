import re

input = []

with open("input.txt","r") as f:
    input = [l.strip() for l in f.read().split("\n\n")]

# Parse Input
entrys = []

for passport in input:
    currentDict = dict()
    for data in re.split(" |\n", passport):
        currentDict[data.split(":")[0]] = data.split(":")[1]
    entrys.append(currentDict)

def entryIsValid(entry):
    reFourDigits = re.compile("^[0-9]{4}$")
    reNineDigits = re.compile("^[0-9]{9}$")
    reNumber = re.compile("^[0-9]+(cm|in)$")
    reSixChars = re.compile("^[0-9a-f]{6}$")  

    eyeColor = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    conditions = [
        not reFourDigits.match(entry["byr"]) or not (1290 <= int(entry["byr"]) <= 2002),
        not reFourDigits.match(entry["iyr"]) or not (2010 <= int(entry["iyr"]) <= 2020),
        not reFourDigits.match(entry["eyr"]) or not (2020 <= int(entry["eyr"]) <= 2030),
        not entry["hcl"].startswith("#") or not reSixChars.match(entry["hcl"][1:]),
        (not reNumber.match(entry["hgt"]) or not entry["hgt"].endswith("cm") 
            or not 150 <= int(entry["hgt"][:-2]) <= 193) and
        (not reNumber.match(entry["hgt"]) or not entry["hgt"].endswith("in") 
            or not 59 <= int(entry["hgt"][:-2]) <= 76), 
        not entry["ecl"] in eyeColor,
        not reNineDigits.match(entry["pid"])
    ]

    if(any(conditions)):
        return 0

    return 1

valids = 0
for entry in entrys:
    if(all(key in entry for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])):
        valids += entryIsValid(entry)

print(valids)