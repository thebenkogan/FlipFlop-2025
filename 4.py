from ff import nums, read_input

lines = read_input()
cs = [tuple(nums(l)) for l in lines]
px, py = 0, 0
total1 = 0
total2 = 0
for x, y in cs:
    xdiff, ydiff = abs(x - px), abs(y - py)
    total1 += xdiff + ydiff
    total2 += abs(xdiff - ydiff) + min(xdiff, ydiff)
    px, py = x, y

print(total1)
print(total2)

total3 = 0
cs = sorted(cs, key=lambda c: c[0] + c[1])
px, py = 0, 0
for x, y in cs:
    xdiff, ydiff = abs(x - px), abs(y - py)
    total3 += abs(xdiff - ydiff) + min(xdiff, ydiff)
    px, py = x, y

print(total3)
