def NGE(arr):
    dOut = {}
    NGEStack = []
    NGEStack.append(arr[0])
    for i in range(1, len(arr)):
        if len(NGEStack) < 0:
            NGEStack.append(arr[i])
            continue
        if arr[i] > NGEStack[-1]:
            while len(NGEStack) > 0 and NGEStack[-1] < arr[i]:
                dOut[NGEStack.pop(0)] = arr[i]
            NGEStack.append(arr[i])
        else:
            NGEStack.append(arr[i])
    if len(NGEStack) != 0:
        while len(NGEStack) != 0:
            dOut[NGEStack.pop(0)] = -1
    return dOut


arr = list(map(int, input().split()))
print(NGE(arr))
