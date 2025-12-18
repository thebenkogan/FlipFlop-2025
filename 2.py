from ff import read_input

lines = read_input(split_lines=False)
h = 0
best = 0
for c in lines:
    if c == "^":
        h += 1
    else:
        h -= 1
    best = max(best, h)

print(best)

h = 0
best = 0
prev = None
f = 1
for c in lines:
    if c != prev:
        f = 1
    else:
        f += 1
    if c == "^":
        h += f
    else:
        h -= f
    best = max(best, h)
    prev = c

print(best)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


i = 0
total = 0
best = 0
while i < len(lines):
    start = i
    curr = lines[i]
    f = 1 if curr == "^" else -1
    while i < len(lines) and lines[i] == curr:
        i += 1
    total += fib(i - start) * f
    best = max(best, total)

print(best)
