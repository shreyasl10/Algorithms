def minCostPath(a, m, n):
    for i in range(1, m):
        a[i][0] += a[i-1][0]

    for i in range(1, n):
        a[0][i] += a[0][i-1]

    for i in range(1, m):
        for j in range(1, n):
            a[i][j] += min(a[i-1][j-1], a[i-1][j], a[i][j-1])

    return a[m-1][n-1]


m = int(input())
a = []
for i in range(m):
    subArray = list(map(int, input().split()))
    a.append(subArray)
n = len(subArray)
print(minCostPath(a, m, n))
