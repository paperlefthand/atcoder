#!/usr/bin/env python3

h, w = [int(i) for i in input().split()]
cols = []
rows = []

for i in range(h):
    s = input()
    for j in range(w):
        if s[j]=='o':
            rows.append(i)
            cols.append(j)

result = abs(rows[0]-rows[1])+abs(cols[0]-cols[1])
print(result)
