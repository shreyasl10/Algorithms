def Bubble(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i]>arr[j]:
                t=arr[i]
                arr[i]=arr[j]
                arr[j]=t
    return arr
arr=list(map(int,input("enter element").split()))
print(Bubble(arr))
