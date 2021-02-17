import re

input = []

with open(r"5\input.txt","r") as f:
    for s in f:
        input.append(s.rstrip())#.split())

regHigh = re.compile("^[R|B]")
regLow = re.compile("^[F|L]")

def binaryPartitioning(directions, data):
    if(len(data) == 1):
        return data[0]
    
    if(directions == ""):
        raise Exception("Not enough instructions")

    if(regLow.match(directions)):
        return binaryPartitioning(directions[1:], data[:len(data)//2])
    elif(regHigh.match(directions)):
        return binaryPartitioning(directions[1:], data[(len(data)//2):])

    raise Exception("Directions invalid")

seatIds = []

for boardingPass in input:
    rowDirections = boardingPass[:-3]
    columnDirections = boardingPass[-3:]
    
    try:
        row = binaryPartitioning(rowDirections, list(range(128)))
        column = binaryPartitioning(columnDirections, list(range(8)))
    except Exception as e:
        print(e.args[0])

    seatIds.append(row*8 + column)

for i in range(1000):
    if(i not in seatIds):
        if(i+1 in seatIds and i-1 in seatIds):
            print (i)


