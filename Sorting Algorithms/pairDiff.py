def pairDiff(arr, k):
    arr.sort()
    l = 0
    r = len(arr)-1
    while l <= r:
        if abs(arr[r]-arr[l]) == k:
            return [arr[l], arr[r]]
        elif abs(arr[r]-arr[l]) > k:
            r -= 1
        else:
            l += 1
    return -1


def pairDiffMap(arr, k):
    diff = {}

    for i in arr:
        if i in diff:
            diff[i] += 1
            if k == 0:
                return [i, i]
        else:
            diff[i] = 1

    if k == 0:
        return -1

    for i in range(len(arr)):
        if arr[i]+k in diff.keys():
            return [arr[i], arr[i]+k]
    return -1


arr = list(map(int, input().split()))
k = int(input())
print(pairDiffMap(arr, k))
