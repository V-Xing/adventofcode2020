import numpy as np
from scipy.signal import convolve2d


def update(seats, occ_neigh, n_vis):
    """ Update `seats` based on the number of visible occupied neighbors `occ_neigh` """
    h, w = seats.shape[0], seats.shape[1]
    next_seats = np.empty_like(seats)
    for i in range(h):
        for j in range(w):
            val = seats[i, j]
            num_neigh = occ_neigh[i, j]
            if val == "L" and num_neigh == 0:
                next_seats[i, j] = "#"
            elif val == "#" and num_neigh >= n_vis:
                next_seats[i, j] = "L"
            else:
                next_seats[i, j] = val
    return next_seats


def q1(seats):
    it = 0
    while it < 10000:
        is_occupied = seats == "#"
        occ_neigh = convolve2d(is_occupied, np.ones((3, 3)), mode="same") - is_occupied
        next_seats = update(seats, occ_neigh, n_vis=4)
        if np.array_equal(seats, next_seats):
            break
        seats = next_seats
        it += 1

    return np.count_nonzero(seats == "#")


def seek_visible_q2(seats):
    """ Seek seats in line-of-sight """
    h, w = seats.shape[0], seats.shape[1]
    visible = {}
    for i in range(h):
        for j in range(w):
            visible[i, j] = []
            for inc, jnc in dirs:
                i0, j0 = i, j
                i0 += inc
                j0 += jnc
                while 0 <= i0 < h and 0 <= j0 < w:
                    if seats[i0, j0] != ".":
                        visible[i, j].append((i0, j0))
                        break
                    i0 += inc
                    j0 += jnc
    return visible


def q2(seats, visible):
    h, w = seats.shape[0], seats.shape[1]
    it = 0
    while it < 10000:
        occ_neigh = np.array(
            [
                [
                    sum([seats[neigh] == "#" for neigh in visible[i, j]])
                    for j in range(w)
                ]
                for i in range(h)
            ]
        )
        next_seats = update(seats, occ_neigh, n_vis=5)
        if np.array_equal(seats, next_seats):
            break
        seats = next_seats
        it += 1
    return np.count_nonzero(seats == "#")


if __name__ == "__main__":
    with open("input.txt") as f:
        seats = np.array([list(line.rstrip()) for line in f])

    print(q1(seats))

    # For q2, first build the array of seats in line-of-sight to avoid doing it every time
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)]
    visible = seek_visible_q2(seats)
    print(q2(seats, visible))
