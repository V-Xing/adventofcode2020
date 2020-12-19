""" Start counting from the end, for q2 accumulate sums whenever possible """

with open("test_input.txt") as f:
    lines = [line.rstrip() for line in f]


def find_opening_parenthesis_rev(op):
    """ Find the index of the opening parenthesis, counting from the end """
    n_par = 0
    for (i, t) in enumerate(reversed(op)):
        n_par += t.count(")")
        n_par -= t.count("(")
        if n_par < 0:
            print("Problem parentheses")
        elif n_par == 0:
            break
    return -i - 1


def q1(op):
    if len(op) == 1:
        return int(op[0])
    elif ")" in op[-1]:
        i = find_opening_parenthesis_rev(op)
        par_res = q1([op[i][1:]] + op[i + 1 : -1] + [op[-1][:-1]])
        return q1(op[:i] + [str(par_res)])
    else:
        res = int(op[-1])
        if op[-2] == "+":
            return res + q1(op[:-2])
        elif op[-2] == "*":
            return res * q1(op[:-2])
        else:
            print("Wrong operator")
            return


def q2(op):
    if len(op) == 1:
        return int(op[0])
    elif ")" in op[-1]:
        i = find_opening_parenthesis_rev(op)
        par_res = q2([op[i][1:]] + op[i + 1 : -1] + [op[-1][:-1]])
        return q2(op[:i] + [str(par_res)])
    else:
        res = int(op[-1])
        plus_idx = len(op) - 2
        while plus_idx > 0 and op[plus_idx] == "+":
            if ")" in op[plus_idx - 1]:
                i = find_opening_parenthesis_rev(op[:plus_idx])
                res += q2(op[:plus_idx][i:])
                plus_idx -= i + 2
            else:
                res += int(op[plus_idx - 1])
                plus_idx -= 2
        if plus_idx <= 0:
            return res
        else:
            return res * q2(op[:plus_idx])


print(sum([q1(line.split()) for line in lines]))
print(sum([q2(line.split()) for line in lines]))
