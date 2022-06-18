def Zeroes(a, low, high):
    if low <= high:
        mid = low+int((high-low)/2)
        if mid == 0 and a[mid] == 1:
            return mid
        elif mid == 0 and a[mid] == 0:
            return -1
        if a[mid] == 0:
            return Zeroes(a, mid+1, high)
        else:
            return Zeroes(a, low, mid-1)
    return -1


arr = list(map(int, input().split()))
c = Zeroes(arr, 0, len(arr)-1)
print(f"C: {c}")
if c == -1:
    print(len(arr))
else:
    print(c)
