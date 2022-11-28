import itertools

N, K = [int(a) for a in input().split()]
T = []
for i in range(N):
    T.append([int(a) for a in input().split()])

count = 0

# aは1,2,...,N-1の置換
for a in itertools.permutations(range(1,N), N-1):
    t = 0
    t += T[0][a[0]]
    for i in range(1, N-1):
        t += T[a[i-1]][a[i]]
    t += T[a[N-2]][0]
    
    if t == K:
        count += 1

print(count)