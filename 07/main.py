import re
from collections import defaultdict

with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

ptrn_head = re.compile("^(.*?) bags contain (\d+) (.*?) bag")
ptrn_body = re.compile("(\d+) (.*?) bag")

in2out = defaultdict(set)  # each color maps to the set of colors that can contain it
out2in = {}  # each color maps to a dict {inner_color: inner_number} of its inner bags

for line in lines:
    split_line = line.split(",")
    head_regex = re.match(ptrn_head, split_line[0])
    if head_regex:
        # If the outer bag contains other bags
        outer = head_regex.group(1)
        num_inner = head_regex.group(2)
        inner = head_regex.group(3)
        in2out[inner].add(outer)
        out2in[outer] = {inner: int(num_inner)}
        for b in split_line[1:]:
            body_regex = re.search(ptrn_body, b)
            num_inner = body_regex.group(1)
            inner = body_regex.group(2)
            in2out[inner].add(outer)
            out2in[outer][inner] = int(num_inner)


def add_to_set(color, in2out, q1):
    """ Add to the `q1` set all the bags that can contain `color` """
    q1.add(color)
    if color in in2out:
        for outers in in2out[color]:
            add_to_set(outers, in2out, q1)


q1 = set()
for outers in in2out["shiny gold"]:
    add_to_set(outers, in2out, q1)

print(len(q1))


def count_bags(color, out2in, count):
    """ Add to the `count` counter the number of bags contained in a `color` bag """
    for inner in out2in[color]:
        if inner in out2in:
            count += out2in[color][inner] * (count_bags(inner, out2in, 0) + 1)
        else:
            count += out2in[color][inner]
    return count


count = 0
print(count_bags("shiny gold", out2in, count))
