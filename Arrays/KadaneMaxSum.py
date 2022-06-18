def MaxSubArray(arr):
	s=0
	m=0
	neg=0
	for i in range(len(arr)):
		if arr[i]<0:
			neg+=1
	if neg==len(arr):
		return max(arr)
	for i in range(len(arr)):
		s+=arr[i]
		if s<0:
			s=0
		if m<s:
			m=s
	return m
arr=list(map(int,input().split()))
print(MaxSubArray(arr))
