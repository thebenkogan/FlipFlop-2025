from ff import nums, read_input

lines = read_input()
birds = [tuple(nums(l)) for l in lines]


def pos_after_t(t):
    return [((t * vx) % 1000, (t * vy) % 1000) for vx, vy in birds]


def in_frame(bs):
    return sum(1 for x, y in bs if 250 <= x < 750 and 250 <= y < 750)


print(in_frame(pos_after_t(100)))


def sum_every(t):
    return sum(in_frame(pos_after_t(t)) for t in range(t, t * 1000 + 1, t))


print(sum_every(3600))
print(sum_every(31556926))
