import numpy as np
from scipy.signal import convolve2d

with open("input.txt") as f:
    splits = f.read().split("\n\n")

tiles = {}
for s in splits:
    tiles[int(s.split("\n")[0].split()[-1][:-1])] = np.array(
        [list(l) for l in s.split("\n")[1:]]
    )

edges = {}
for (k, t) in tiles.items():
    edges[k] = [
        t[0],
        t[0][::-1],
        t[:, 0],
        t[:, 0][::-1],
        t[-1],
        t[-1][::-1],
        t[:, -1],
        t[:, -1][::-1],
    ]


def find_match_to_edge(x, edges, used):
    """
    Given an edge `x`, the index in `edges` of the matching piece that can match it
    except for the pieces in `used`
    """

    return [
        k
        for (k, list_e) in edges.items()
        if k not in used
        for e in list_e
        if (x == e).all()
    ]


def transforms(t):
    f = np.flip(t, 1)
    return [
        t,
        np.rot90(t),
        np.rot90(t, 2),
        np.rot90(t, 3),
        f,
        np.rot90(f),
        np.rot90(f, 2),
        np.rot90(f, 3),
    ]


corners = []
prod = 1
for (k, v) in edges.items():
    # For each piece, count the number of edges that do not have a match
    # i.e. find_match_to_edge returns an empty list
    # If it is a corner piece, this number is 4 (2 edges + their reflections)
    if sum([not m for m in [find_match_to_edge(e, edges, {k}) for e in v]]) == 4:
        prod *= k
        corners.append(k)
print(prod)

h = next(iter(tiles.values())).shape[0]
n = int(len(tiles) ** (1 / 2))
puzzle = np.empty((n, n), dtype=int)  # contains the tile ids
image = np.empty((n * h, n * h), dtype=str)  # contains the tiles
used = set()  # incrementally collects the pieces we use

# Set the top-left corner and find its edges that have a match
puzzle[0, 0] = piece = corners[0]
topleft_edges = []
for (k, v) in edges.items():
    if k != piece:
        e1 = edges[piece]
        for e in v:
            for i in range(8):
                if (e1[i] == e).all():
                    topleft_edges.append(i)

# Transform the piece so that the two distinct edges in topleft_edges are the bottom and
# right edge
for t in transforms(tiles[piece]):
    if np.all(t[:, -1] == edges[piece][topleft_edges[0]]) and np.all(
        t[-1] == edges[piece][topleft_edges[2]]
    ):
        image[:h, :h] = t
        break
edge_right = edges[piece][topleft_edges[0]]

# Build the top row by matching right edges
for j in range(1, 12):
    piece = find_match_to_edge(edge_right, edges, used)[0]
    puzzle[0, j] = piece
    # We found the right piece (assuming only one exists), now transform it until its
    # left edge corresponds to the right edge of the previous piece
    for t in transforms(tiles[piece]):
        if np.all(t[:, 0] == edge_right):
            image[:h, j * h : (j + 1) * h] = t
            break
    edge_right = t[:, -1]
    used.add(piece)

# Build the rest of the puzzle column-by-column by matching bottom edges
for j in range(12):
    edge_bot = image[h - 1, j * h : (j + 1) * h]
    piece = puzzle[0, j]
    for i in range(1, 12):
        piece = find_match_to_edge(edge_bot, edges, used)[0]
        puzzle[i, j] = piece
        for t in transforms(tiles[piece]):
            if np.all(t[0] == edge_bot):
                image[i * h : (i + 1) * h, j * h : (j + 1) * h] = t
                break
        edge_bot = t[-1]
        used.add(piece)

# Remove tile borders and binarize the image
image = np.delete(
    image, list(range(0, n * h, h)) + list(range(h - 1, n * h, h)), axis=0
)
image = np.delete(
    image, list(range(0, n * h, h)) + list(range(h - 1, n * h, h)), axis=1
)
image = image == "#"

# Build the monster mask
idxs_monster = [
    [0, 18],
    [1, 0],
    [1, 5],
    [1, 6],
    [1, 11],
    [1, 12],
    [1, 17],
    [1, 18],
    [1, 19],
    [2, 1],
    [2, 4],
    [2, 7],
    [2, 10],
    [2, 13],
    [2, 16],
]

n_monster = len(idxs_monster)

monster = np.zeros((3, 20), dtype=int)
idxs_monster = np.transpose(np.array(idxs_monster))
monster[idxs_monster[0], idxs_monster[1]] = 1

# For each transform, convolve it with the monster mask and check where all the monster
# pixels were found (conv result = n_monster)
occ_monster = [
    np.sum(convolve2d(img, monster, mode="valid") == n_monster)
    for img in transforms(image)
]
assert np.count_nonzero(occ_monster) == 1

print(np.sum(image) - max(occ_monster) * n_monster)
