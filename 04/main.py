import re

with open("input.txt") as f:
    lines = f.read()

arr = lines.split("\n\n")  # array of passports
arr = [p.replace("\n", " ") for p in arr]  # make it a bit nicer

req_flds = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

ptrn_fld = re.compile("\w+(?=:)")

print(sum([all(f in re.findall(ptrn_fld, pspt) for f in req_flds) for pspt in arr]))

ptrn_val = re.compile("(?<=:)[^\s]+")
conds = {
    "byr": "(19[2-9][0-9]|200[0-2])$",
    "iyr": "(201[0-9]|2020)$",
    "eyr": "(202[0-9]|2030)$",
    "hgt": "((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)$",
    "hcl": "\#[0-9a-f]{6}$",
    "ecl": r"\b(amb|blu|brn|gry|grn|hzl|oth)\b",
    "pid": r"\b[0-9]{9}\b",
}


count = 0
for pspt in arr:
    pspt_flds = re.findall(ptrn_fld, pspt)
    if all(f in pspt_flds for f in req_flds):
        pspt_vals = re.findall(ptrn_val, pspt)
        count += all(
            [
                re.match(conds[fld], val)
                for (fld, val) in zip(pspt_flds, pspt_vals)
                if fld in req_flds
            ]
        )

print(count)

# One-liner!
print(
    sum(
        [
            all(
                [
                    re.match(conds[fld], val)
                    for (fld, val) in zip(
                        re.findall(ptrn_fld, pspt), re.findall(ptrn_val, pspt)
                    )
                    if fld in req_flds
                ]
            )
            for pspt in arr
            if all(f in re.findall(ptrn_fld, pspt) for f in req_flds)
        ]
    )
)
