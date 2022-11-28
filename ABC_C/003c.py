#!/usr/bin/env python3

from typing import List

def main(k: int, rates: List[int]) -> float:
    result = 0.0
    rates_top_k = sorted(rates, reverse=True)[:k]
    for r in reversed(rates_top_k):
        result = (result + r) / 2

    return result

if __name__ == '__main__':
    n, k = (int(x) for x in input().split())
    rates = [int(r) for r in input().split()]
    result = main(k, rates)
    print(result)

