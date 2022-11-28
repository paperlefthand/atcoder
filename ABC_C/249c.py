def main():
    n, k = [int(i) for i in input().split()]
    texts = [input() for _ in range(n)]

    result = 0
    for i in range(1 << n):
        count = [0] * 26
        for j in range(n):
            if bool(i & (1<<j)):
                for l in range(26):
                    if chr(l+97) in texts[j]:
                        count[l] += 1
        result = max(result, len([x for x in count if x == k]))

    return result


print(main())
    