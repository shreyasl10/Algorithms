
def ZeroesEnd(arr):
    l = 0
    r = len(arr)-1
    while l < r:
        if arr[l] == 0 and arr[r] == 0:
            r -= 1
        elif arr[l] == 0 and arr[r] != 0:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        elif arr[l] != 0 and arr[r] == 0:
            l += 1
            r -= 1
        else:
            l += 1
    print('After shift: ', arr)


arr = list(map(int, input().split()))
print('Before shift : ', arr)
ZeroesEnd(arr)
