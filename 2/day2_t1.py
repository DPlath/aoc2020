input = []

with open(r"2\input.txt","r") as f:
    for s in f:
        input.append(s.rstrip())

valid = 0

for password in input:
    policy, pw = [s.strip() for s in password.split(":")[0:2]]
    numbers, character = [s.strip() for s in policy.split(" ")[0:2]]
    firstNumber, secondNumber = [int(i) for i in numbers.split("-")[0:2]]

    if(pw.count(character) in range(firstNumber,secondNumber + 1)):
        valid += 1

print(valid)


