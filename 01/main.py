with open("input.txt") as f:
    lines = [int(line.rstrip()) for line in f]

print(lines)

for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        if lines[i] + lines[j] == 2020:
            print(lines[i] * lines[j])
            break

for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        for k in range(j + 1, len(lines)):
            if lines[i] + lines[j] + lines[k] == 2020:
                print(lines[i] * lines[j] * lines[k])
                break
