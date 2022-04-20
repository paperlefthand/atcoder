#!/usr/bin/env python3
import math

def count_digit(a, b):
    return max(len(str(a)), len(str(b)))

def main(n: int) -> int:

    result = count_digit(n, n)
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            result = min(result, count_digit(i, n//i))
        i += 1
    return result

if __name__ == '__main__':
    N = int(input())
    print(main(N))