def Counting(arr):
	m=max(arr)
	output=[0]*len(arr)
	count=[0]*(m+1)
	for i in range(len(arr)):
		count[arr[i]]+=1
	for i in range(1,len(count)):
		count[i]+=count[i-1]
	i=len(arr)-1
	while(i>=0):
		output[count[arr[i]]-1]=arr[i]
		count[arr[i]]-=1
		i-=1
	for i in range(len(arr)):
		arr[i]=output[i]
	return arr
arr=list(map(int,input().split()))
print(Counting(arr))
