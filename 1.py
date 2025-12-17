from ff import read_input


lines = read_input()
total1 = 0
total2 = 0
total3 = 0
for line in lines:
    l = line.count("n") + 1
    total1 += l
    if l % 2 == 0:
        total2 += l
    if "e" not in line:
        total3 += l

print(total1)
print(total2)
print(total3)
