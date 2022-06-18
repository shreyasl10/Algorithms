def LinearSearch(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1
arr=list(map(int,input("Enter the array\n").split()))
key=int(input("Enter the element to be searched "))
index=LinearSearch(arr,key)
if index!=-1:
    print(f"Element found at index {index}")
else:
    print("Element not found")
