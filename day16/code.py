import collections
import re
import sys

ranges, your, neighbor = [l.rstrip('\n') for l in sys.stdin.read().split('\n\n')]

rp = []
rpd = collections.defaultdict(list)
for line in ranges.splitlines():
    kind = line.split(': ')[0]
    for a, b in re.findall(r'(\d+)-(\d+)', line):
        rp.append((int(a), int(b), kind))
        rpd[kind].append((int(a), int(b)))

fail = 0
valtix = []
for line in neighbor.splitlines()[1:]:
    nums = [int(l) for l in line.split(',')]
    any_fail = False
    for num in nums:
        if any(a <= num <= b for a, b, _ in rp):
            pass
        else:
            fail += num
            any_fail = True
    if not any_fail:
        valtix.append(nums)
print(fail)

your_p = [int(l) for l in your.splitlines()[1].split(',')]
valtix.append(your_p)

over_under = collections.defaultdict(list)
num_f = len(valtix[0])
for f in range(len(valtix[0])):
    over_under[f] = [t[f] for t in valtix]

memo = {}


def can_match(fname, im):
    k = (fname, im)
    if k in memo:
        return memo[k]
    cm = all(any(a <= v <= b for a, b in rpd[fname]) for v in over_under[im])
    memo[k] = cm
    return cm


assign = {}
assign_b = {}
while len(rpd) > len(assign):
    progress = False
    for im in range(num_f):
        if im in assign_b.keys():
            continue
        t = []
        for f_name in rpd.keys():
            if f_name in assign.keys():
                continue
            if can_match(f_name, im):
                t.append(f_name)
        if len(t) == 1:
            assign[t[0]] = im
            assign_b[im] = t[0]
            # print(im, 'is', t)

prod = 1
for f_name, im in assign.items():
    if f_name.startswith('departure'):
        print(f_name, your_p[im])
        prod *= your_p[im]
print(prod)
