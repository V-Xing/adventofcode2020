from collections import defaultdict

with open("input.txt") as f:
    lines = [int(line.rstrip()) for line in f]

lines = sorted(lines)

n1j = 0
n3j = 0
cur_jolt = 0

for j in lines:
    diff = j - cur_jolt
    if diff == 1:
        n1j += 1
    elif diff == 3:
        n3j += 1
    elif diff != 2:
        print(f"Jolt {j} is not valid")
        break
    cur_jolt = j

print(n1j * (n3j + 1))

lines.insert(0, 0)
nb_arr = {}
parents = {}

for (idx, j) in enumerate(lines[1:]):
    parents[j] = [k for k in lines[max(0, idx - 2) : idx + 1] if j - k <= 3]

nb_arr[0] = 1
for j in lines[1:]:
    nb_arr[j] = sum([nb_arr[k] for k in parents[j]])

print(nb_arr[lines[-1]])
