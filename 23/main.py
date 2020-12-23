import numpy as np

# Leaving my lazy numpy initial implementation which critically fails for part 2
with open("input.txt") as f:
    cups = np.array([int(c) for c in f.readline()])

n = len(cups)
for i in range(100):
    cur = cups[0]
    taken = cups[1:4]
    cups = np.delete(cups, [1, 2, 3])
    dest_idx = np.argmin((cur - cups[1:]) % n)
    cups = np.insert(cups, dest_idx + 2, taken)
    cups = np.roll(cups, -1)

while cups[0] != 1:
    cups = np.roll(cups, -1)
print("".join(str(c) for c in cups[1:]))


with open("input.txt") as f:
    start = [int(c) for c in f.readline()]

succ = {}  # succ[i] is the cup immediately clockwise of cup i
for (i, c) in enumerate(start[:-1]):
    succ[c] = start[(i + 1) % len(start)]
succ[start[-1]] = len(start) + 1
for i in range(len(start) + 1, 1000000):
    succ[i] = i + 1
succ[1000000] = start[0]

cur = start[0]
n = len(succ)
for i in range(10000000):
    next1 = succ[cur]
    next2 = succ[next1]
    next3 = succ[next2]
    dest = cur - 1 if cur > 1 else n
    while dest in [next1, next2, next3]:
        dest = dest - 1 if dest > 1 else n
    succ[cur] = succ[next3]
    succ[next3] = succ[dest]
    succ[dest] = next1
    cur = succ[cur]

print(succ[1] * succ[succ[1]])
