from collections import Counter
from ff import nums, read_input

lines = read_input()
cs = [tuple(nums(l)) for l in lines]
counts = Counter(cs)

print(counts.most_common()[0][0])


def color(c):
    r, g, b = c
    if r == g or g == b or r == b:
        return "special"
    elif r > g and r > b:
        return "red"
    elif g > r and g > b:
        return "green"
    else:
        return "blue"


colored = list(map(color, cs))
print(sum(1 for c in colored if c == "green"))

m = {
    "red": 5,
    "green": 2,
    "blue": 4,
    "special": 10,
}
print(sum(m[c] for c in colored))
