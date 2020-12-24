import re
from collections import defaultdict


def move(x, y, step):
    return {
        "e": (x + 1, y),
        "se": (x + 0.5, y - 0.5),
        "sw": (x - 0.5, y - 0.5),
        "w": (x - 1, y),
        "nw": (x - 0.5, y + 0.5),
        "ne": (x + 0.5, y + 0.5),
    }[step]


with open("input.txt") as f:
    tiles = [line.rstrip() for line in f]

black = set()
for tile in tiles:
    x, y = 0, 0
    steps = re.findall(r"(e|se|sw|w|nw|ne)", tile)
    for step in steps:
        x, y = move(x, y, step)
    if ((x, y)) not in black:
        black.add((x, y))
    else:
        black.remove((x, y))

print(len(black))

for _ in range(100):
    adj = {}
    adj = defaultdict(lambda: 0, adj)  # maps tile to the number of its black neighbors
    for (x, y) in black:
        for neigh in [
            (x + 1, y),
            (x + 0.5, y + 0.5),
            (x + 0.5, y - 0.5),
            (x - 1, y),
            (x - 0.5, y + 0.5),
            (x - 0.5, y - 0.5),
        ]:
            adj[neigh] += 1
    black &= set(adj.keys())  # remove black tiles without black neighbors
    for (tile, num_adj) in adj.items():
        if tile in black and num_adj > 2:
            black.remove(tile)
        elif tile not in black and num_adj == 2:
            black.add(tile)

print(len(black))
