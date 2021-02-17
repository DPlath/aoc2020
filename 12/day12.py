from math import sin, cos, radians


def readInput(day):
    with open(str(day) + r"\input.txt", "r") as f:
        input = [l.strip() for l in f.read().split("\n")]
    return input


moves = ["N", "S", "W", "E"]
headings = {"N": 0, "E": 90, "S": 180, "W": 270}


def move(direction, length, x, y):
    if(direction == "N"):
        y -= length
    elif(direction == "S"):
        y += length
    elif(direction == "E"):
        x += length
    elif(direction == "W"):
        x -= length

    return x, y


def rotate(direction, length, facing):
    currentDegree = headings[facing]

    if(direction == "L"):
        currentDegree -= length
    else:
        currentDegree += length

    currentDegree = currentDegree % 360

    for head in headings:
        if(headings[head] == currentDegree):
            return head


def part1(input):
    facing = "E"
    x, y = 0, 0

    for pa_call in input:
        direction = pa_call[0]
        length = int(pa_call[1:])

        if(direction in moves):
            x, y = move(direction, length, x, y)
        elif(direction == "F"):
            x, y = move(facing, length, x, y)
        else:
            facing = rotate(direction, length, facing)

    return abs(x)+abs(y)


def rotateWaypoint(x, y, wp_x, wp_y, direction, length):
    if(direction == "L"):
        length *= -1

    tempX, tempY = wp_x - x, wp_y - y
    rad = radians(length)
    sinus, cosinus = round(sin(rad)), round(cos(rad))

    wp_x = (tempX * cosinus - tempY * sinus) + x
    wp_y = (tempX * sinus + tempY * cosinus) + y

    return int(wp_x), int(wp_y)

def part2(input):
    wp_x, wp_y = 10, -1
    x, y = 0, 0

    for pa_call in input:
        direction = pa_call[0]
        length = int(pa_call[1:])

        if(direction in moves):
            wp_x, wp_y = move(direction, length, wp_x, wp_y)
        elif(direction == "F"):
            for _ in range(length):
                dist_x, dist_y = wp_x - x, wp_y - y
                x = wp_x
                y = wp_y
                wp_x += dist_x
                wp_y += dist_y
        else:
            wp_x, wp_y = rotateWaypoint(x, y, wp_x, wp_y, direction, length)
    
    return abs(x)+abs(y)


input = readInput(12)
print("Lösung von Part 1: {}".format(part1(input.copy())))
print("Lösung von Part 2: {}".format(part2(input.copy())))
