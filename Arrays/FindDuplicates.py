# Question
# Given an array of length n+1 containing values(a[i]) where 1<=a[i]<=n. There exists one duplicate element occuring more than once while the rest of the elements occur once. Find that duplicate element.
#
# Sample Input
# 1 4 2 5 2 3
#
# Sample Output
# 2

def Duplicates(arr):
    for i in range(len(arr)):
        x = abs(arr[i])
        if arr[x-1] < 0:
            return x
        arr[x-1] = -(arr[x-1])


arr = list(map(int, input().split()))
print(Duplicates(arr))
