def water(h):
    if len(h)==0:
        return 0
    min_h = min(h)
    i = h.index(min_h)
    h = [a-min_h for a in h]
    return min_h+water(h[:i])+water(h[i+1:])

def main():
    N = int(input())
    h = [int(a) for a in input().split()]
    print(water(h))

main()