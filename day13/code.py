import collections
import math
import re
import sys

lines = [l.rstrip('\n') for l in sys.stdin]


def chinese(pairs):
    bubu = 1
    for x, mx in pairs:
        bubu *= mx
    bubu_zuzu = 0
    for x, mx in pairs:
        zuzu = bubu // mx
        bubu_zuzu += x * zuzu * pow(zuzu, mx - 2, mx)
        bubu_zuzu %= bubu
    return bubu_zuzu


start = int(lines[0])
pairs = []
for i, n in enumerate(lines[1].split(',')):
    if n == 'x':
        continue
    n = int(n)
    pairs.append((n - i, n))
    print(pairs)
print(chinese(pairs))
