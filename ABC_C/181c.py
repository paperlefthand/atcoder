def main():
    N = int(input())
    coordinates = []
    for _ in range(N):
        x, y = input().split()
        coordinates.append((int(x), int(y)))
    coordinates.sort(key=lambda x: x[0])

    for i in range(N):
        a1, b1 = coordinates[i]
        for j in range(i+1, N):
            a2, b2 = coordinates[j]
            for (a3, b3) in coordinates[j+1:]:
                if (a3-a1)*(b2-b1)==(b3-b1)*(a2-a1):
                    return 'Yes'   
    return 'No'
    
print(main())