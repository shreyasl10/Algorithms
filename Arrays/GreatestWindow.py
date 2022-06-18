

# Question:
# Given an array A of size 'N' and an integer k, find the maximum for each and every contiguous subarray of size k.
#
# Sample Input
# 1 2 3 1 4 5 2 3 6
# 3
#
# Sample Output
# 3 3 4 5 5 5 6

def Greatest(arr, k):
    de = []
    output = []
    for i in range(k):
        while de and arr[de[-1]] < arr[i]:
            de.pop()
        de.append(i)
    for i in range(k, len(arr)):
        output.append(arr[de[0]])
        while de and de[0] <= i-k:
            de.pop(0)
        while de and arr[de[0]] < arr[i]:
            de.pop()
        de.append(i)
    output.append(arr[de[0]])
    return output


arr = list(map(int, input().split()))
k = int(input())
print(Greatest(arr, k))
