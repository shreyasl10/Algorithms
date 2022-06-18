def slidingWindow(arr, k):
    window = sum(arr[:k])
    max_sum = window
    for i in range(len(arr)-k):
        window = window-arr[i]+arr[i+k]
        max_sum = max(max_sum, window)
    return max_sum


arr = list(map(int, input().split()))
k = int(input())
print(slidingWindow(arr, k))
