input = []


with open(r"1\input.txt","r") as f:
    for s in f.readlines():
        input.append(int(s.rstrip()))

for i in range(len(input)):
    # Alle Summen berechnen von i+1 bis len
    for j in range(i+1,len(input)):
        # Summe bilden und checken
        if(input[i] + input[j] == 2020):
            print(input[i])
            print(input[j])
            print("{} * {} = {}".format(input[i],input[j],input[i]*input[j]))
            exit(0)