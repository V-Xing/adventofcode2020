import re

with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

n_valid = 0
for line in lines:
    regex = re.search("(.*)-(.*) (.*): (.*)", line)
    low_num = int(regex.group(1))
    high_num = int(regex.group(2))
    char = regex.group(3)
    string = regex.group(4)
    if low_num <= string.count(char) <= high_num:
        n_valid += 1

print(n_valid)

n_valid = 0
for line in lines:
    regex = re.search("(.*)-(.*) (.*): (.*)", line)
    low_num = int(regex.group(1))
    high_num = int(regex.group(2))
    char = regex.group(3)
    string = regex.group(4)
    if (string[low_num - 1] == char) ^ (string[high_num - 1] == char):
        n_valid += 1

print(n_valid)
