from itertools import cycle

with open("input.txt") as f:
    lines = [line.rstrip() for line in f]


def q1():
    cards = cycle(["E", "S", "W", "N"])
    pos = [0, 0]  # east, north
    facing = next(cards)
    for line in lines:
        tkn = line[0]
        val = int(line[1:])

        if tkn == "L":
            if val == 90:
                for i in range(3):
                    facing = next(cards)
            elif val == 180:
                for i in range(2):
                    facing = next(cards)
            elif val == 270:
                facing = next(cards)
            else:
                print("Unknown rotation value")
                break
            val = 0
        elif tkn == "R":
            if val == 90:
                facing = next(cards)
            elif val == 180:
                for i in range(2):
                    facing = next(cards)
            elif val == 270:
                for i in range(3):
                    facing = next(cards)
            else:
                print("Unknown rotation value")
                break
            val = 0
        elif tkn == "F":
            moving = facing
        else:
            moving = tkn

        if moving == "N":
            pos[1] += val
        elif moving == "S":
            pos[1] -= val
        elif moving == "E":
            pos[0] += val
        elif moving == "W":
            pos[0] -= val

    return abs(pos[0]) + abs(pos[1])


print(q1())


def q2():
    wpt_x, wpt_y = 10, 1  # east, north relative to ship
    ship_x, ship_y = 0, 0
    for line in lines:
        tkn = line[0]
        val = int(line[1:])

        if tkn == "L":
            if val == 90:
                wpt_x, wpt_y = -wpt_y, wpt_x
            elif val == 180:
                wpt_x, wpt_y = -wpt_x, -wpt_y
            elif val == 270:
                wpt_x, wpt_y = wpt_y, -wpt_x
            else:
                print("Unknown rotation value")
                break
        elif tkn == "R":
            if val == 90:
                wpt_x, wpt_y = wpt_y, -wpt_x
            elif val == 180:
                wpt_x, wpt_y = -wpt_x, -wpt_y
            elif val == 270:
                wpt_x, wpt_y = -wpt_y, wpt_x
            else:
                print("Unknown rotation value")
                break
        elif tkn == "F":
            ship_x += val * wpt_x
            ship_y += val * wpt_y
        elif tkn == "N":
            wpt_y += val
        elif tkn == "S":
            wpt_y -= val
        elif tkn == "E":
            wpt_x += val
        elif tkn == "W":
            wpt_x -= val

    return abs(ship_x) + abs(ship_y)


print(q2())
