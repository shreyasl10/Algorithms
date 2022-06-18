def minPoints(startX, endX):
    count = 0
    result = 0
    while count != 2:
        m = 0
        r = 0
        for i in range(len(startX)):
            if endX[i]-startX[i] > m:
                m = (endX[i]-startX[i])
                r = i
        out = [startX[i], endX[i]]
        indices = []
        for i in range(len(startX)):
            if startX[i] not in range(out[0], out[1]+1):
                indices.append(i)

        startX = [startX[i] for i in range(len(startX)) if i not in indices]
        endX = [endX[i] for i in range(len(endX)) if i not in indices]
        result += 1
        count = len(startX)+len(endX)
        print(startX)
        print(endX)
        if count == 0:
            break
    if count == 0:
        return result
    elif count == 2:
        return result+1


start = list(map(int, input().split()))
stop = list(map(int, input().split()))
print(minPoints(start, stop))
