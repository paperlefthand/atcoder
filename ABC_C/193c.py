import math 

N = int(input())
nums = set()

a = 2
while a <= math.sqrt(N):
    b = 2
    while a**b <= N:
        nums.add(a**b) 
        b += 1
    a += 1

print(N-len(nums))