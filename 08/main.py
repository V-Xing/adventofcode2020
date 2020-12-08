with open("input.txt") as f:
    lines = [line.rstrip() for line in f]


def is_loop_finite(lines):
    seen = set()
    acc = 0
    i = 0
    while len(seen) < len(lines):
        if i in seen:
            return False, acc
            break
        elif i > len(lines) - 1:
            return True, acc
            break
        else:
            seen.add(i)
        line = lines[i]
        tkn = line[:3]
        if tkn == "nop":
            i += 1
            continue
        elif tkn == "acc":
            acc += int(line[4:])
            i += 1
            continue
        elif tkn == "jmp":
            i += int(line[4:])
            continue
        else:
            print("Unrecognized token")
            break
    print("Uncontrolled exit of while loop")
    return


finite, acc = is_loop_finite(lines)
assert not finite
print(f"Q1: {acc}")


seen = set()
acc = 0
i = 0
inf_loop = False
while len(seen) < len(lines):
    if i in seen:
        print("Q2: Found an infinite loop")
        break
    elif i > len(lines) - 1:
        print("Q2: Exhausted lines")
        break
    else:
        seen.add(i)
    line = lines[i]
    tkn = line[:3]
    if tkn == "nop":
        lines[i] = lines[i].replace("nop", "jmp")
        finite, acc_mod = is_loop_finite(lines)
        if finite:
            print(f"Q2: {acc_mod}")
            break
        lines[i] = lines[i].replace("jmp", "nop")
        i += 1
        continue
    elif tkn == "acc":
        acc += int(line[4:])
        i += 1
        continue
    elif tkn == "jmp":
        lines[i] = lines[i].replace("jmp", "nop")
        finite, acc_mod = is_loop_finite(lines)
        if finite:
            print(f"Q2: {acc_mod}")
            break
        lines[i] = lines[i].replace("nop", "jmp")
        i += int(line[4:])
        continue
    else:
        print("Q2: Unrecognized token")
        break
