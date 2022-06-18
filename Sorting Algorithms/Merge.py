def Merge(arr):
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        L=Merge(L)
        R=Merge(R)
        arr=[]
        while len(L)>0 and len(R)>0:
            if L[0]<R[0]:
                arr.append(L[0])
                L.pop(0)
            else:
                arr.append(R[0])
                R.pop(0)
        for i in L:
                arr.append(i)
        for i in R:
                arr.append(i)
    return arr
arr=list(map(int,input().split()))
a=Merge(arr)
print(*a)
        
