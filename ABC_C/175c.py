def main():
    x, k, d = [int(i) for i in input().split()]
    x = abs(x)

    if x - k*d == 0:
        return 0

    if x - k*d > 0:
        return (x-k*d)

    q = x // d

    if (k - q) % 2 == 0:
        result = min(x-q*d, abs(x-(q+2)*d))
        return result    
    else:
        result = min(x-(q-1)*d, abs(x-(q+1)*d))
        return result    

result = main()
print(result)