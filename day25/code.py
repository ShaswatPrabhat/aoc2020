import sys

lines = [l.rstrip('\n') for l in sys.stdin]
a, b = [int(i) for i in lines]


def get_key(inp):
    for i in range(100000000):
        if pow(7, i, 20201227) == inp:
            return i


print(pow(a, get_key(b), 20201227))
print(pow(b, get_key(a), 20201227))
