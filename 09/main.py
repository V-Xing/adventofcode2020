from collections import deque

with open("input.txt") as f:
    lines = [int(line.rstrip()) for line in f]

n_prev = 25

q = deque()
for n in lines[:n_prev]:
    q.append(n)

for n in lines[n_prev:]:
    if any([(n - k != k) and (n - k in q) for k in q]):
        q.popleft()
        q.append(n)
    else:
        n_weak = n
        print(n_weak)
        break

sums = []  # sums[i] = sum(lines[:i])
cur_sum = 0
# Fill sums incrementally until the end of the contiguous range is located by looking
# for sums[i]-n_weak in sums
for (cur_idx, n) in enumerate(lines):
    cur_sum += n
    sums.append(cur_sum)
    try:
        start_idx = sums.index(cur_sum - n_weak)
        print(max(lines[start_idx + 1 : cur_idx]) + min(lines[start_idx + 1 : cur_idx]))
        break
    except ValueError:
        continue
