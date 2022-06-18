def MaxHeapify(arr, i, n):
    largest = i
    left = 2*i+1
    right = 2*i+2

    if left >= n and right >= n:
        return

    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        MaxHeapify(arr, largest, n)


def kthLargest(arr, k):
    output = 0
    for i in range(len(arr)//2-1, -1, -1):
        MaxHeapify(arr, i, len(arr))
    for i in range(len(arr)-1, k-1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        output = arr[i]
        MaxHeapify(arr, 0, i)
    return output


arr = list(map(int, input().split()))
k = int(input())
print(kthLargest(arr, k))
