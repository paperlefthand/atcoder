#!/usr/bin/env python3

import math

def main(n: int):

    divs_upper = []

    i = 1
    while i < math.sqrt(n):
        if n % i == 0:
            print(i)
            divs_upper.append(n//i)
        i += 1
    
    if math.sqrt(n).is_integer():
        print(int(math.sqrt(n)))

    for s in divs_upper[::-1]:
        print(s)

if __name__ == '__main__':
    N = int(input())
    main(N)