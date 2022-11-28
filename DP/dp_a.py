n = int(input())
costs = [int(c) for c in input().split()]
memo = [0] * n
memo[1] = abs(costs[0]-costs[1])

for i in range(2, n):
    c1 = abs(costs[i-2]-costs[i])+memo[i-2]
    c2 = abs(costs[i-1]-costs[i])+memo[i-1]
    memo[i] = min(c1, c2)

print(memo[-1])