n, m = [int(i) for i in input().split()]

# pairs = set()
# for i in range(m):
#     a, b = [int(i) for i in input().split()]
#     if a>b:
#         b, a = a, b
#     pairs.add((a, b))
# pairs = list(pairs)

pairs = []
for i in range(m):
    a, b = [int(i) for i in input().split()]
    pairs.append((int(a), int(b)))

a, b = pairs[0]
s = {a, b}
groups = [s]

for (a, b) in pairs[1:]:
    for s in groups:
        if (a in s or b in s):
            s.add(a)
            s.add(b)
            break
    s_new = {a, b}
    groups.append(s_new)

print(max([len(s) for s in groups]))