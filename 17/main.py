"""
Store every cube with padding to allow for the creation of active neighbors at the
edges. Not as smart as just storing the indices of the active cubes (sparsely) but numpy
go brrrrr
"""

import numpy as np
from scipy.ndimage import convolve


def update_q1(grid, act_neigh):
    """ Update 3D `grid` based on the number of active neighbors `act_neigh` """
    h, w, d = grid.shape
    next_grid = np.empty_like(grid)
    pad = np.zeros(6, dtype=int)
    for i in range(h):
        for j in range(w):
            for k in range(d):
                num_neigh = act_neigh[i, j, k]
                if grid[i, j, k]:
                    next_grid[i, j, k] = num_neigh == 2 or num_neigh == 3
                else:
                    if num_neigh == 3:
                        next_grid[i, j, k] = 1
                        pad[
                            np.where(
                                np.array(
                                    [
                                        i == 0,
                                        i == h - 1,
                                        j == 0,
                                        j == w - 1,
                                        k == 0,
                                        k == d - 1,
                                    ]
                                )
                            )
                        ] = 1
                    else:
                        next_grid[i, j, k] = 0
    return np.pad(next_grid, ((pad[0], pad[1]), (pad[2], pad[3]), (pad[4], pad[5])))


def update_q2(grid, act_neigh):
    """ Update 4D `grid` based on the number of active neighbors `act_neigh` """
    h, w, d, e = grid.shape
    next_grid = np.empty_like(grid)
    pad = np.zeros(8, dtype=int)
    for i in range(h):
        for j in range(w):
            for k in range(d):
                for l in range(e):
                    num_neigh = act_neigh[i, j, k, l]
                    if grid[i, j, k, l]:
                        next_grid[i, j, k, l] = num_neigh == 2 or num_neigh == 3
                    else:
                        if num_neigh == 3:
                            next_grid[i, j, k, l] = 1
                            pad[
                                np.where(
                                    np.array(
                                        [
                                            i == 0,
                                            i == h - 1,
                                            j == 0,
                                            j == w - 1,
                                            k == 0,
                                            k == d - 1,
                                            l == 0,
                                            l == e - 1,
                                        ]
                                    )
                                )
                            ] = 1
                        else:
                            next_grid[i, j, k, l] = 0
    return np.pad(
        next_grid,
        ((pad[0], pad[1]), (pad[2], pad[3]), (pad[4], pad[5]), (pad[6], pad[7])),
    )


def q1(start):
    h, w = start.shape
    grid = np.zeros((h, w, 3), dtype=int)
    grid[:, :, 1] = start == "#"
    grid = np.pad(grid, ((1, 1), (1, 1), (0, 0)))

    for i in range(6):
        act_neigh = convolve(grid, np.ones((3, 3, 3)), mode="constant") - grid
        grid = update_q1(grid, act_neigh)

    return np.sum(grid)


def q2(start):
    h, w = start.shape
    grid = np.zeros((h, w, 3, 3), dtype=int)
    grid[:, :, 1, 1] = start == "#"
    grid = np.pad(grid, ((1, 1), (1, 1), (0, 0), (0, 0)))

    for i in range(6):
        act_neigh = convolve(grid, np.ones((3, 3, 3, 3)), mode="constant") - grid
        grid = update_q2(grid, act_neigh)

    return np.sum(grid)


if __name__ == "__main__":
    with open("input.txt") as f:
        start = np.array([list(line.rstrip()) for line in f])

    print(q1(start))
    print(q2(start))
