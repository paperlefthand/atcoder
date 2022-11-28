#!/usr/bin/env python3

h, w = [int(i) for i in input().split()]
r, c = [int(i) for i in input().split()]

result = 4

if h==1:
    result -= 2
elif r==1 or r==h:
    result -= 1

if w == 1:
    result -= 2
elif c==1 or c==w:
    result -= 1

print(result) 
