def minPlatforms(arr, dep):

    arr.sort()
    dep.sort()

    platforms = 1
    result = 1
    n = len(arr)
    i = 1
    j = 0

    while i < n and j < n:
        if arr[i] <= dep[j]:
            platforms += 1
            i += 1
        elif arr[i] > dep[j]:
            platforms -= 1
            j += 1

        result = max(result, platforms)
    return result


arr = list(map(int, input().split()))
dep = list(map(int, input().split()))

print(minPlatforms(arr, dep))
