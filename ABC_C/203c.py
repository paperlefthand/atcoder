#!/usr/bin/env python3

def main(n, k, list_a, list_b):
    b = 0
    for i in range(n):
        if (k - list_a[i] + b) < 0:
            return k + b
        else:
            b += list_b[i]
    return k + b

if __name__ == '__main__':
    n, k = map(int, input().split())
    inputs = []
    for _ in range(n):
        a, b = input().split()
        inputs.append((int(a), int(b)))
    inputs.sort(key = lambda x:x[0])
    list_a = [a for (a, _) in inputs]
    list_b = [b for (_, b) in inputs]

    result = main(n, k, list_a, list_b)

    print(result)