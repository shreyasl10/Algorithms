def maxOnes(a, m, n):
    maxOnes = 0
    index = n-1
    for i in range(m):
        flag = False
        while index >= 0 and a[i][index] == 1:
            flag = True
            if flag:
                maxOnes = max(maxOnes, i)
            index -= 1

    if maxOnes == 0 and a[m][n-1] == 0:
        return 0
    return maxOnes


m = int(input())
a = []
for i in range(m):
    subArray = list(map(int, input().split()))
    a.append(subArray)
n = len(subArray)
print(maxOnes(a, m, n))
