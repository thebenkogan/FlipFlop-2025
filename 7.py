from functools import cache
from ff import nums, read_input

lines = read_input()
sizes = [tuple(nums(l)) for l in lines]


@cache
def num_ways(pos, end):
    if pos == end:
        return 1
    elif any(a > b for a, b in zip(pos, end)):
        return 0
    total = 0
    pos = list(pos)
    for i in range(len(pos)):
        pos[i] += 1
        total += num_ways(tuple(pos), end)
        pos[i] -= 1
    return total


print(sum(num_ways((0, 0), (w - 1, h - 1)) for w, h in sizes))
print(sum(num_ways((0, 0, 0), (w - 1, h - 1, w - 1)) for w, h in sizes))
print(sum(num_ways(tuple([0] * d), tuple([s - 1] * d)) for d, s in sizes))
