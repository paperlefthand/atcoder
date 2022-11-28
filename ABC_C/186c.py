#!/usr/bin/env python3

def n_adic(q):
    digits = []
    digits.append(q % 8)
    q = q // 8
    while q>0:
        digits.append(q % 8)
        q = q // 8
    return digits

def main(n: int) -> int:

    result = n
    for i in range(1, 1+n):
        if ('7' in str(i)):
            result -= 1
        elif (7 in n_adic(i)):
            result -= 1

    return result

if __name__ == '__main__':
    N = int(input())
    print(main(N))