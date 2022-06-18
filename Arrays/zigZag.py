def zigZag(arr):
    for i in range(1, len(arr), 2):
        if arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
        if arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]


arr = list(map(int, input().split()))
zigZag(arr)
print(arr)
