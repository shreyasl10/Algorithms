def rotateMatrix(a, m, n):
    top = 0
    bottom = m-1
    left = 0
    right = n-1

    while left <= right and top <= bottom:
        prev = a[top+1][left]
        # Top Row
        for i in range(left, right+1):
            cur = a[top][i]
            a[top][i] = prev
            prev = cur
        top += 1

        # Right Column
        for i in range(top, bottom+1):
            cur = a[i][right]
            a[i][right] = prev
            prev = cur
        right -= 1

        # Bottom row
        for i in range(right, left-1, -1):
            cur = a[bottom][i]
            a[bottom][i] = prev
            prev = cur
        bottom -= 1

        # Left Column
        for i in range(bottom, top-1, -1):
            cur = a[i][left]
            a[i][left] = prev
            prev = cur
        left += 1
    return a


m = int(input())
a = []
for i in range(m):
    subArray = list(map(int, input().split()))
    a.append(subArray)
n = len(subArray)
output = rotateMatrix(a, m, n)
for i in range(m):
    for j in range(n):
        print(output[i][j], end=' ')
    print()
