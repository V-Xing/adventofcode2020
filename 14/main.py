import re
from itertools import chain, combinations

with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

memory = {}
for line in lines:
    if line.split()[0] == "mask":
        mask = [(i, c) for i, c in enumerate(line.split()[-1]) if c != "X"]
    else:
        add = re.findall("(?<=\[)(.*?)(?=\])", line)[0]
        num = int(line.split()[-1])
        bin_num = list(f"{num:036b}")
        for m in mask:
            bin_num[m[0]] = m[1]
        memory[add] = int("".join(bin_num), 2)

print(sum(memory.values()))


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


memory = {}
for line in lines:
    if line.split()[0] == "mask":
        mask = line.split()[-1]
    else:
        num = int(line.split()[-1])
        add = int(re.findall("(?<=\[)(.*?)(?=\])", line)[0])
        bin_add = list(f"{add:036b}")
        for (i, c) in enumerate(mask):
            if c != "0":
                bin_add[i] = c
        # We just need to deal with the Xs now
        pos_X = [i for i, c in enumerate(bin_add) if c == "X"]
        combs = list(powerset(pos_X))
        adds = set()
        # Make all possible addresses from `combs` and add them to `adds`
        for comb in combs:
            bin_add_comb = []
            for (i, b) in enumerate(bin_add):
                if i in pos_X:
                    if i in comb:
                        bin_add_comb.append("1")
                    else:
                        bin_add_comb.append("0")
                else:
                    bin_add_comb.append(b)
            add_comb = int("".join(bin_add_comb), 2)
            adds.add(add_comb)

        for add in adds:
            memory[add] = num

print(sum(memory.values()))
