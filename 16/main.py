import re

valid = set()
ranges = []
nearby = []
with open("input.txt") as f:
    splits = f.read().split("\n\n")

for line in splits[0].split("\n"):
    starts = re.findall("(\d+)(?=-)", line)
    ends = re.findall("(?<=-)(\d+)", line)
    assert len(starts) == len(ends) == 2
    range0 = range(int(starts[0]), int(ends[0]) + 1)
    range1 = range(int(starts[1]), int(ends[1]) + 1)
    valid.update(set(range0) | set(range1))
    ranges.append(set(range0) | set(range1))

my_tkt = [int(x) for x in splits[1].split("\n")[1].split(",")]

err_rate = 0
for line in splits[2].split("\n")[1:]:
    tkt = [int(x) for x in line.split(",")]
    if set(tkt) - valid:
        err_rate += sum(set(tkt) - valid)
    else:
        nearby.append(tkt)

print(err_rate)

val_pos = [
    [j + 1 for j in range(len(ranges)) if all([tkt[j] in rg for tkt in nearby])]
    for rg in ranges
]
# For a field i, val_pos[i] contains the valid positions (shifted to start at 1)
# It turns out the valid positions of each field are all nested within each other
# so we can find the valid positions iteratively by starting with the field with only 1
# valid position

# Sort val_pos by length while keeping the original indices
srtd_val_pos = sorted(enumerate(val_pos), key=lambda i: len(i[1]))

# Incrementally build the dictionary mapping from position to field
pos_to_fld = {}
for pos in srtd_val_pos:
    for p in pos[1]:
        if p not in pos_to_fld:
            pos_to_fld[p] = pos[0] + 1

departure_pos = [k for k, v in pos_to_fld.items() if v <= 6]

prod = 1
for pos in departure_pos:
    prod *= my_tkt[pos - 1]

print(prod)
