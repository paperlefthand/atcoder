#!/usr/bin/env python3

from functools import reduce
from typing import List

def main(times: List[int]) -> int:
    result = reduce(lcm, times)
    return result

def gcd(a: int, b: int) -> int:
    """ 最小公倍数
    """
    a, b = abs(a), abs(b)
    if a<b:
        a, b = b, a

    r = 0
    while b > 0:
        r = a % b
        a, b = b, r

    return a

def lcm(a: int, b: int) -> int:
    """ 最大公約数
    """
    l = a*b // gcd(a,b)
    return l

if __name__ == '__main__':
    n = int(input())
    times = []
    for i in range(n):
        times.append(int(input()))
    print(main(times))
