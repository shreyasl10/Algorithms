def MinHeapify(arr, n, i):
    smallest = i
    left = 2*i+1
    right = 2*i+2

    if left >= n and right >= n:
        return
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        MinHeapify(arr, n, smallest)


def MergeSorted(arr, k):
    Heap = []
    output = []
    for i in arr:
        Heap.append(i[0])

    for i in range(len(Heap)//2-1, -1, -1):
        MinHeapify(Heap, len(Heap), i)

    while len(Heap) > 0:
        output.append(Heap.pop(0))
        for i in arr:
            if len(i) > 0 and i[0] == output[-1]:
                i.pop(0)
                if len(i) > 0:
                    Heap.append(i[0])
                break
        for i in range(len(Heap)//2-1, -1, -1):
            MinHeapify(Heap, len(Heap), i)

    return output


k = int(input())
arr = []
for i in range(k):
    tempArr = list(map(int, input().split()))
    arr.append(tempArr)
print(MergeSorted(arr, k))
