def trappingRain(arr):
    output = 0
    for i in range(1, len(arr)-1):

        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])

        right = arr[i]
        for j in range(i, len(arr)):
            right = max(right, arr[j])

        output += min(left, right)-arr[i]
    return output


def trappingRainOptimized(arr):
    low = 0
    high = len(arr)-1
    result = 0
    left_max = 0
    right_max = 0
    while low <= high:
        if arr[low] < arr[high]:
            if arr[low] > left_max:
                left_max = arr[low]
            else:
                result += left_max-arr[low]
            low += 1
        else:
            if arr[high] > right_max:
                right_max = arr[high]
            else:
                result += right_max-arr[high]
            high -= 1
    return result


arr = list(map(int, input().split()))
print(trappingRain(arr))
print(trappingRainOptimized(arr))
