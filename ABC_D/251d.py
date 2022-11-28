#!/usr/bin/env python3

n = int(input())
arr = [int(a) for a in input().split()]

cost1 = arr[0]
i = 3
while(i <= n):
    if arr[i-1]+arr[i+1]<arr[i]:
        



# n, w = [int(i) for i in input().split()]
# list_a = [int(i) for i in input().split()] 
# list_a.sort()
# ws = [0]*w

# for a in list_a:
#     if a <= w:
#         ws[a-1] = 1

# for i in range(n):
#     for j in range (i+1, n):
#         sum = list_a[i]+list_a[j]
#         if sum > w:
#             break
#         else:
#             ws[sum-1] = 1

# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j+1, n): 
#             sum = list_a[i]+list_a[j]+list_a[k]
#             if sum > w:
#                 break
#             else:
#                 ws[sum-1] = 1

# print(ws.count(1))

