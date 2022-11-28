def main():
    S = [int(x)%3 for x in input()]
    a, b = 0, 0
    for s in S:
        if s==1:
            a += 1
        elif s==2:
            b += 1

    # a, b: mod=1,2の個数カウント
    # i: 何桁消すか
    d = min(a+b+1, len(S))
    for i in range(d):
        _a, _b = a, b
        for j in range(i+1):
            _a, _b = a-j, b-(i-j)
            if _a>=0 and _b>=0 and (_a-_b)%3==0:
                return i
    return -1
            
result = main()
print(result)