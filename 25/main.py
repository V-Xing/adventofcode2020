with open("input.txt") as f:
    card_pub = int(f.readline().rstrip())
    door_pub = int(f.readline().rstrip())

card_loop = 0
subject = 7
value = 1
while True:
    value = (subject * value) % 20201227
    card_loop += 1
    if value == card_pub:
        break

door_loop = 0
subject = 7
value = 1
while True:
    value = (subject * value) % 20201227
    door_loop += 1
    if value == door_pub:
        break

subject = card_pub
encryption = 1
for _ in range(door_loop):
    encryption = (subject * encryption) % 20201227

print(encryption)
