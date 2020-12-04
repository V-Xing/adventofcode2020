import numpy as np

with open("input.txt") as f:
    lines = np.array([list(line.rstrip()) for line in f])

arr = lines == "#"
height, width = lines.shape


def count_trees(arr, right, down):
    # Not tested if height % down != 0 (no examples provided)
    # Didn't find a way to use :: with right-side periodicity, so very ugly
    return np.sum(
        [arr[down * i, right * i % width] for i in range((height - 1) // down + 1)]
    )


right_list = [1, 3, 5, 7, 1]
down_list = [1, 1, 1, 1, 2]

print(count_trees(arr, 3, 1))
print(
    np.prod(
        [count_trees(arr, right_list[i], down_list[i]) for i in range(len(right_list))]
    )
)
