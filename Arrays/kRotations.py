def PrintKRotations(arr, k):
    k = k % len(arr)
    for i in range(len(arr)):
        if i < k:
            print(arr[len(arr)+i-k], end=" ")
        else:
            print(arr[i-k], end=" ")


def KRotatesBrute(arr, k):
    k = k % len(arr)
    for i in range(k):
        last = arr[-1]
        for j in range(len(arr)-1, 0, -1):
            arr[j] = arr[j-1]
        arr[0] = last
    print(arr)


def KRotatesAuxiliary(arr, k):
    k = k % len(arr)
    = [arr[len(arr)-k+i] for i in range(k)]
    for i in range(len(arr)-k):
        arr[i+k] = arr[i]
    for i in range(len(aux)):
        arr[i] = aux[i]
    print(arr)


def Swap(arr, low, high):
    while low < high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1


def KRotatesOptimized(arr, n, k):
    Swap(arr, n-k, n-1)
    Swap(arr, 0, n-k-1)
    Swap(arr, 0, n-1)
    print(arr)


arr = list(map(int, input().split()))
k = int(input())
# PrintKRotations(arr, k)
# print()
# KRotatesBrute(arr, k)
# print()
#KRotatesAuxiliary(arr, k)
# print()
KRotatesOptimized(arr, len(arr), k)
