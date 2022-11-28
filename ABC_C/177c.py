N = int(input())
nums = [int(a) for a in input().split()]

s = sum(nums)
result = 0
m = 7 + 10**9

for i in range(N-1):
    s -= nums[i]
    result += (nums[i]*s) % m

print(result % m)