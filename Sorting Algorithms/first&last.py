def First(arr, k):
    l = 0
    h = len(arr)-1
    index = -1

    while l <= h:
        mid = (l+h)//2
        if arr[mid] > k:
            h = mid-1
        elif arr[mid] < k:
            l = mid+1
        else:
            index = mid
            h = mid-1
    return index


def Last(arr, k):
    l = 0
    h = len(arr)-1
    index = -1

    while l <= h:
        mid = (l+h)//2
        if arr[mid] > k:
            h = mid-1
        elif arr[mid] < k:
            l = mid+1
        else:
            index = mid
            l = mid+1
    return index


arr = list(map(int, input().split()))
k = int(input())
print('First occurence is : ', First(arr, k))
print('Last occurence is : ', Last(arr, k))
