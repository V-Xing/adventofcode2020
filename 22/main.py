from collections import deque


def read_input(input_file):
    q1 = deque()
    q2 = deque()
    with open(input_file) as f:
        splits = f.read().split("\n\n")
    for c in splits[0].split("\n")[1:]:
        q1.append(int(c))
    for c in splits[1].split("\n")[1:]:
        q2.append(int(c))
    return q1, q2


def compute_score(qwin):
    res = 0
    i = 1
    while qwin:
        res += qwin.pop() * i
        i += 1
    return res


def part1(q1, q2):
    while q1 and q2:
        c1 = q1.popleft()
        c2 = q2.popleft()
        if c1 > c2:
            q1.append(c1)
            q1.append(c2)
        else:
            q2.append(c2)
            q2.append(c1)
    winner = q1 if q1 else q2
    return compute_score(winner)


def rec_combat(q1, q2):
    seen = set()
    while q1 and q2:
        state = (tuple(q1), tuple(q2))
        if state in seen:
            return 1, q1, q2
        else:
            seen.add(state)

        c1 = q1.popleft()
        c2 = q2.popleft()

        if c1 <= len(q1) and c2 <= len(q2):
            copy1 = deque(list(q1)[:c1])
            copy2 = deque(list(q2)[:c2])
            rd_winner, _, _ = rec_combat(copy1, copy2)
        else:
            rd_winner = 1 if c1 > c2 else 2

        if rd_winner == 1:
            q1.append(c1)
            q1.append(c2)
        else:
            q2.append(c2)
            q2.append(c1)

    game_winner = 2 if q2 else 1
    return game_winner, q1, q2


q1, q2 = read_input("input.txt")
print(part1(q1, q2))

q1, q2 = read_input("input.txt")
game_winner, q1, q2 = rec_combat(q1, q2)
qwin = q1 if game_winner == 1 else q2
print(compute_score(qwin))
