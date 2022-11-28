#!/usr/bin/env python3
S = input()[::-1]

counts = [0]*2019
counts[0] = 1
num=0
d=1

for s in S:
    num += int(s)*d
    num %= 2019
    # これがダメなのはメモリの消費量の問題??
    # num_mod = num % 2019
    # counts[num_mod] += 1
    counts[num] += 1
    d *= 10
    d %= 2019
 
result = 0
 
for c in counts:
    result += (c*(c-1)//2)
 
print(result)