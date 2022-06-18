def Selection(arr):
	for i in range(len(arr)):
		m=i
		for j in range(i+1,len(arr)):
			if arr[m]>arr[j]:
				m=j
		arr[i],arr[m]=arr[m],arr[i]
	return arr
arr=list(map(int,input().split()))
print(Selection(arr))
 
