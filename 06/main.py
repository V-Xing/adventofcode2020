with open("test_input.txt") as f:
    lines = f.read()

arr = lines.split("\n\n")

arr1 = [p.replace("\n", "") for p in arr]  # list of concatenated group answers
print(sum([len(set(p)) for p in arr1]))

arr2 = [p.split("\n") for p in arr]  # list of list of group answers per person
print(
    len(
        [
            c
            for (p1, p2) in zip(arr1, arr2)
            for c in set(p1)
            if all([c in q for q in p2])
        ]
    )
)
