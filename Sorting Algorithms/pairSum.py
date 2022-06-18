def pairSum(arr, k):
    arr.sort()
    l = 0
    r = len(arr)-1
    while l <= r:
        if arr[r]+arr[l] == k:
            return [arr[l], arr[r]]
        elif arr[r]+arr[l] > k:
            r -= 1
        else:
            l += 1
    return -1


def pairSumMap(arr, k):
    sums = {}

    for i in range(len(arr)):
        if abs(arr[i]-k) in sums.keys():
            return [arr[i], arr[i]+k]
        sums[arr[i]] = i
    return -1


arr = list(map(int, input().split()))
k = int(input())
print(pairSum(arr, k))
