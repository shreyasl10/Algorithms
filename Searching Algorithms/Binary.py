def BinarySearch(arr,key):
    low=0
    high=len(arr)-1
    while(low<high):
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            high=mid-1
        else:
            low=mid+1
    return -1
arr=list(map(int,input("Enter the array\n").split()))
key=int(input("Enter the element to be searched "))
#Sort the array in ascending order before passing it to the function. Binary search does not work on unsorted arrays.
arr.sort()
index=BinarySearch(arr,key)
if index!=-1:
    print(f"Element found at index {index}")
else:
    print("Element not found")
