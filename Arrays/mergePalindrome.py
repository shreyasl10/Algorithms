def mergePalindrome(arr):
    l, r = 0, len(arr)-1
    count = 0
    while l <= r:
        if arr[l] == arr[r]:
            l += 1
            r -= 1
        elif arr[l] < arr[r]:
            l += 1
            arr[l] += arr[l-1]
            count += 1
        else:
            r -= 1
            arr[r] -= arr[r+1]
            count += 1
    return count


arr = list(map(int, input().split()))
print(mergePalindrome(arr))
