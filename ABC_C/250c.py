n, q = [int(i) for i in input().split()]
arr = [i for i in range(1, n+1)]
for _ in range(q):
  x = int(input())
  arr[x-1] = 1 if arr[x-1]==n else arr[x-1]+1
  arr[x%n] = n if arr[x%n]==1 else arr[x%n]-1
print(arr)