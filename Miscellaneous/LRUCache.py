def LRU(inp, arr, size):
    f = 0
    if size != 0:
        if inp in arr.keys():
            f = 1
        if f == 1:
            arr.pop(inp)
        arr[inp] = 1
        size -= 1

    # else:
arr = {}
size = int(input())
inpu = int(input())
while inpu != -1:
    LRU(inpu, arr, size)
    print(arr)
    inpu = int(input())
