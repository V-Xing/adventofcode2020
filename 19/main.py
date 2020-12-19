import re

with open("input.txt") as f:
    splits = f.read().split("\n\n")

rules = {}
for line in splits[0].split("\n"):
    k, v = line.split(": ")
    rules[k] = v


def regex_q1(rule):
    if '"' in rule:  # rule is "a" or "b"
        return rule[1]
    elif "|" not in rule:
        return "".join([regex_q1(rules[r]) for r in rule.split()])
    else:
        or1, or2 = rule.split("|")  # the input rules contain at most one |
        return "(" + regex_q1(or1) + "|" + regex_q1(or2) + ")"


def regex_q2(rule):
    if rule == "42 | 42 8":
        return regex_q2(rules["42"]) + "+"
    elif rule == "42 31 | 42 11 31":
        r42 = regex_q2(rules["42"])
        r31 = regex_q2(rules["31"])
        # re can't ensure that we have the same number of 42 and 31 patterns
        # So try to match exactly 1 to 10 occurrences of 42 with the same number of 31
        # 10 is enough given the length of the messages
        return "(?:" + "|".join(f"{r42}{{{i}}}{r31}{{{i}}}" for i in range(1, 10)) + ")"
    if '"' in rule:
        return rule[1]
    elif "|" not in rule:
        return "".join([regex_q2(rules[r]) for r in rule.split()])
    else:
        or1, or2 = rule.split("|")
        return "(?:" + regex_q2(or1) + "|" + regex_q2(or2) + ")"


regex1 = re.compile(r"^" + regex_q1(rules["0"]) + "$")
print(sum([bool(regex1.match(msg)) for msg in splits[1].split("\n")]))

rules["8"] = "42 | 42 8"
rules["11"] = "42 31 | 42 11 31"
regex2 = re.compile(r"^" + regex_q2(rules["0"]) + "$")
print(sum([bool(regex2.match(msg)) for msg in splits[1].split("\n")]))
