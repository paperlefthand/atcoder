#!/usr/bin/env python3

n, a, b = [int(i) for i in input().split()]

row_white = True

i=0
while(i<n):
    for _ in range(a):
        col_white = row_white
        row = ''
        j = 0
        while(j<n):
            row += ('.'*b if col_white else '#'*b)
            col_white = not col_white
            j+=1
        print(row)
    row_white = not row_white
    i += 1

