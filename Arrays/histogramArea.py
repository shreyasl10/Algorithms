def areaHistogram(histogram):
    stack = []
    max_area = 0
    index = 0

    while index < len(histogram):
        if not stack or histogram[stack[-1]] <= histogram[index]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            if stack:
                area = histogram[top]*(index-stack[-1]-1)
            else:
                area = histogram[top]*(index)
            max_area = max(max_area, area)
    while stack:
        top = stack.pop()
        if stack:
            area = histogram[top]*(index-stack[-1]-1)
        else:
            area = histogram[top]*(index)
        max_area = max(max_area, area)
    return max_area


histogram = list(map(int, input().split()))
print(areaHistogram(histogram))
