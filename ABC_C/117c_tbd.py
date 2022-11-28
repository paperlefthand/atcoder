#TBD
# 

def solve(xs):
    x_min, x_max = xs[0], xs[-1]
    result = 0
    if x_max>x_min:
        mean = (x_max+x_min) /  2
        x_middle_under = max([i for i in xs if i < mean])
        x_middle_over = min([i for i in xs if i > mean])
        result = (x_middle_under - x_min) + (x_max - x_middle_over)
        if mean in xs:
            result += min(mean-x_middle_under, x_middle_over-mean)

    return result

def main():
    n, m = [int(a) for a in input().split()]
    xs = [int(a) for a in input().split()]

    if n>=m:
        return 0
    
    xs.sort()

    if n==1:
        return abs(max(xs)-min(xs))

    # 持ち駒を両端から置いていく
    i = (n-1) // 2
    if n%2==0:
        result = solve(xs[i:m-i])
    else:
        result = min(solve(xs[i:m-(i-1)]), solve(xs[i-1:m-i]))

    # 2 : [0:m] 0
    # 3 : [1:m] or [0:m-1] 1
    # 4 : [1:m-1] 1
    # 5 : [2:m-1] or [1:m-2] 2
    # 6 : [2:m-2] 2

    
    # result = solve(xs, n)
    # if n % 2 == 0:
    #     result = solve(xs, n)
    # else:
    #     result = min(solve(xs[(n-1)//2:-n//2]), solve(xs[n//2:-(n-1)//2]))

    return result

print(main())
