def count(a, b, c):
    n2, n3, n4 = a, b, c
    result = 0
    
    reduce_count = min(n4//2, n2)
    result += reduce_count
    n4 = n4 - 2*reduce_count
    n2 = n2 - reduce_count
    
    reduce_count = min(n4, n3//2)
    result += reduce_count
    n4 = n4 - reduce_count
    n3 = n3 - 2*reduce_count

    reduce_count = min(n4, n2//3)
    result += reduce_count
    n4 = n4 - reduce_count
    n2 = n2 - 3*reduce_count

    reduce_count = min(n3//2, n2//2)
    result += reduce_count
    n3 = n3 - 2*reduce_count
    n2 = n2 - 2*reduce_count

    result += (n2//5)

    return result

def main():
    N = int(input())
    for _ in range(N):
        a,b,c = list(map(int, input().split()))
        print(count(a,b,c))

main()


    