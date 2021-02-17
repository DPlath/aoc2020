from queue import Queue


def readInput(day):
    with open(str(day) + r"\input.txt", "r") as f:
        input = [l.strip() for l in f.read().split("\n\n")]
    return input


def parseInput(input):
    gameSetup = []

    for player in input:
        cards = Queue()
        player = player.split("\n")
        player = player[1:]

        for i in range(len(player)):
            cards.put(int(player[i]))

        gameSetup.append(cards)

    return gameSetup


def round(player1, player2):
    c1 = player1.get()
    c2 = player2.get()

    if(c1 > c2):
        player1.put(c1)
        player1.put(c2)
    else:
        player2.put(c2)
        player2.put(c1)


def getScore(player):
    score = 0
    for mult, i in enumerate(reversed(player.queue), start=1):
        score += i * mult

    return score


def recGame(allCards):
    player1 = allCards[0]
    player2 = allCards[1]
    player1States = list()
    player2States = list()

    while(player1.qsize() > 0 and player2.qsize() > 0):
        p1State = list(player1.queue)
        p2State = list(player2.queue)
        winner = 0

        if(p1State in player1States or p2State in player2States):
            return 1, p1State

        player1States.append(p1State)
        player2States.append(p2State)

        c1 = player1.get()
        c2 = player2.get()

        if(c1 <= player1.qsize() and c2 <= player2.qsize()):
            p1Sub = list(player1.queue)[:c1]
            p2Sub = list(player2.queue)[:c2]

            p1QSub = Queue()
            p2QSub = Queue()

            for i in p1Sub:
                p1QSub.put(i)
            
            for i in p2Sub:
                p2QSub.put(i)


            allCardsSub = [p1QSub, p2QSub]
            winner, _ = recGame(allCardsSub)

        else:
            if(c1 > c2):
                winner = 1
            else:
                winner = 2

        if(winner == 1):
            player1.put(c1)
            player1.put(c2)
        else:
            player2.put(c2)
            player2.put(c1)

    if(player1.qsize() > player2.qsize()):
        winner = 1
        state = list(player1.queue)
    else:
        winner = 2
        state = list(player2.queue)

    return winner, state


def part1(allCards):
    player1 = allCards[0]
    player2 = allCards[1]

    while(player1.qsize() > 0 and player2.qsize() > 0):
        round(player1, player2)

    winner = max(player1, player2, key=lambda q: q.qsize())

    return getScore(winner)


def part2(allCards):
    _, state = recGame(allCards)

    q = Queue()
    for i in state:
        q.put(i)

    return getScore(q)



input = readInput(22)
allCards = parseInput(input)
allCards2 = parseInput(input)

print("Lösung von Part 1: {}".format(part1(allCards)))
print("Lösung von Part 2: {}".format(part2(allCards2)))
