def spiralOrder(a, m, n):
    top = 0
    bottom = m-1
    left = 0
    right = n-1
    output = []
    direction = 0
    while top <= bottom and left <= right:
        if direction == 0:
            for i in range(left, right+1):
                output.append(a[top][i])
            direction += 1
            top += 1
        elif direction == 1:
            for i in range(top, bottom+1):
                output.append(a[i][right])
            direction += 1
            right -= 1
        elif direction == 2:
            for i in range(right, left-1, -1):
                output.append(a[bottom][i])
            direction += 1
            bottom -= 1
        elif direction == 3:
            for i in range(bottom, top-1, -1):
                output.append(a[i][left])
            direction = 0
            left += 1
    return output


m = int(input())
a = []
for i in range(m):
    subArray = list(map(int, input().split()))
    a.append(subArray)
n = len(subArray)
print(spiralOrder(a, m, n))
