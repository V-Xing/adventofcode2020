from math import gcd

with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

ready = int(lines[0])
pos = []
buses = []
prod = 1
for (i, val) in enumerate(lines[1].split(",")):
    if val != "x":
        pos.append(i)
        buses.append(int(val))
        prod *= int(val)

lowest = ready
for bus in buses:
    if bus - ready % bus < lowest:
        lowest = bus - ready % bus
        best_bus = bus

print(best_bus * lowest)


def euclid(a, b):
    r, u, v, r2, u2, v2 = a, 1, 0, b, 0, 1
    while r2 != 0:
        q = r // r2
        r, u, v, r2, u2, v2 = r2, u2, v2, r - q * r2, u - q * u2, v - q * v2
    return r, u, v


assert all([gcd(a, b) == 1 for (a, b) in zip(buses, buses) if a != b])

# Chinese remainder theorem
# Find x s.t. x%n=-p for p, n in pos, buses
# x = sum_i -p_i * (prod_{k!=i} n_k) * invmod(prod_{k!=i} n_k, n_i) [mod prod_i n_i]
# With Python < 3.8, implement invmod with Euclid algorithm
x = 0
for (p, n) in zip(pos, buses):
    temp = prod // n
    r, u, v = euclid(temp, n)
    assert r == 1
    x += (-p) * temp * u

# Find smallest positive candidate
if x < 0:
    while x < 0:
        x += prod
else:
    while x - prod > 0:
        x -= prod

print(x)
