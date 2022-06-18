def Partition(arr, l, h):
    pivot = arr[h]
    i = l-1
    for j in range(l, h):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return i+1


def Quick(arr, l, h):
    if l >= h:
        return
    j = Partition(arr, l, h)
    Quick(arr, l, j-1)
    Quick(arr, j+1, h)


arr = list(map(int, input().split()))
Quick(arr, 0, len(arr)-1)
print(arr)
