with open("input.txt") as f:
    nums = f.readline().split(",")

last_turn = {}
for (i, n) in enumerate(nums):
    last_turn[int(n)] = i + 1

last = 0
for i in range(len(nums) + 2, 30000001):
    last_turn[last], last = i - 1, i - 1 - last_turn[last] if last in last_turn else 0
    if i == 2020:
        print(last)

print(last)
