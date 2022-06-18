def Heapify(a, n, i):
    largest = i
    l = (2*i)+1
    r = (2*i)+2

    if l >= n and r >= n:
        return
    if l < n and a[largest] < a[l]:
        largest = l
    if r < n and a[largest] < a[r]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        Heapify(a, n, largest)


def HeapSort(a):
    n = len(a)
    for i in range(n//2 - 1, -1, -1):
        Heapify(a, n, i)
    # print(a)
    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        # print(a)
        Heapify(a, i, 0)


arr = list(map(int, input().split()))
HeapSort(arr)
print(arr)
