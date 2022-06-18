def MinHeapify(arr, i, n):
    smallest = i
    left = 2*i+1
    right = 2*i+2

    if left >= n and right >= n:
        return

    if left < n and arr[smallest] > arr[left]:
        smallest = left
    if right < n and arr[smallest] > arr[right]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        MinHeapify(arr, smallest, n)


def kthSmallest(arr, k):
    output = 0
    for i in range(len(arr)//2-1, -1, -1):
        MinHeapify(arr, i, len(arr))
    for i in range(len(arr)-1, k-1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        output = arr[i]
        MinHeapify(arr, 0, i)
    return output


arr = list(map(int, input().split()))
k = int(input())
print(kthSmallest(arr, k))
