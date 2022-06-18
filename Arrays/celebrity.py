def celebrity(a, n):
    candidate = -1
    l = 0
    h = n-1
    while l < h:
        if a[h][l] == 1:
            h -= 1
        else:
            l += 1
    candidate = l
    for k in range(n):
        if candidate != k:
            if a[k][candidate] == 0 or a[candidate][k] == 1:
                return -1
    return candidate


a = []
m = int(input())
for i in range(m):
    temp = list(map(int, input().split()))
    a.append(temp)
print(celebrity(a, m))
