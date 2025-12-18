from collections import defaultdict
from ff import read_input

lines = read_input(split_lines=False)
pairs = defaultdict(list)
tunnels = set()
for i, c in enumerate(lines):
    pairs[c].append(i)
    tunnels.add(c)

adj = {}
for _, (s, e) in pairs.items():
    adj[s] = e
    adj[e] = s

curr = 0
total1 = 0
total3 = 0
seen = set()
while curr < len(lines):
    seen.add(lines[curr])
    nxt = adj[curr]
    total1 += abs(nxt - curr)
    f = 1 if lines[curr].islower() else -1
    total3 += f * abs(nxt - curr)
    curr = nxt + 1

print(total1)

diff = list(tunnels.difference(seen))
diff = sorted(diff, key=lambda c: min(pairs[c]))
print("".join(diff))

print(total3)
