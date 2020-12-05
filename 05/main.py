with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

ids = []
for line in lines:
    row = int("".join("1" if c == "B" else "0" for c in line[:7]), 2)
    col = int("".join("1" if c == "R" else "0" for c in line[7:]), 2)
    id_ = 8 * row + col
    ids.append(id_)

srtd = sorted(ids)

print(srtd[-1])
print([x + 1 for (i, x) in enumerate(srtd[:-1]) if srtd[i + 1] == x + 2][0])
