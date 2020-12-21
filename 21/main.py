from collections import defaultdict

foods = []  # array from line number to set of foods in this line
allergens = defaultdict(list)  # dictionary from allergen name to lines it is found in
with open("input.txt") as f:
    for (i, line) in enumerate(f):
        line = line.rstrip()
        splits = line.split("(")
        foods.append(set(splits[0].split()))
        for allergen in splits[1][9:-1].split(", "):
            allergens[allergen].append(i)

# For any allergen, the foods that can contain it are the ones found in common in the
# lines containiing the allergen
can_have_allergen = set.union(
    *[set.intersection(*[foods[i] for i in l]) for l in allergens.values()]
)

cannot_have_allergen = set.union(*foods) - can_have_allergen

print(sum([food in line for line in foods for food in cannot_have_allergen]))

# Map allergens to the foods that can contain them
all_to_foods = {}
for (k, v) in allergens.items():
    all_to_foods[k] = set.intersection(*[foods[i] for i in v]) - cannot_have_allergen

# Assume we can solve by elimination: iteratively find the allergen that has a single
# unseen food
seen = set()
while len(seen) < len(allergens):
    for (k, v) in all_to_foods.items():
        if len(v - seen) == 1:
            all_to_foods[k] = v - seen
            seen |= v

print(",".join([all_to_foods[key].pop() for key in sorted(all_to_foods.keys())]))
