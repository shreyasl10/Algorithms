def MinDiff(arr, n, k):
    arr.sort()
    minDiff = arr[n-1]-arr[0]
    small = arr[0]+k
    large = arr[n-1]-k
    for i in range(len(arr)):
        minValue = min(small, arr[i]+k)
        maxValue = max(large, arr[i]-k)
        if minValue < 0:
            continue
        minDiff = min(minDiff, (maxValue-minValue))
    return minDiff


arr = list(map(int, input().split()))
k = int(input())
print(MinDiff(arr, len(arr), k))
