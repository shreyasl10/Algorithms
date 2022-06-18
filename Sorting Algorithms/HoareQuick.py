def Partition(arr, l, h):
    pivot = arr[l]
    i = l-1
    j = h+1
    while(i < j):
        while(True):
            i += 1
            if arr[i] >= pivot:
                break
        while(True):
            j -= 1
            if arr[j] <= pivot:
                break
        if(i < j):
            arr[i], arr[j] = arr[j], arr[i]
    return j


def Quick(arr, l, h):
    if l >= h:
        return
    j = Partition(arr, l, h)
    Quick(arr, l, j)
    Quick(arr, j+1, h)


arr = list(map(int, input().split()))
Quick(arr, 0, len(arr)-1)
print(arr)
