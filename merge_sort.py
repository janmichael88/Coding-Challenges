a = list(range(0,30,2))
b = list(range(1,30,2))
print(a)
print(b)

def merge(left,right):
	#two sepearte lists are already ordered
	result = []
	left_idx, right_idx = 0,0
	while left_idx < len(left) and right_idx < len(right):
		if left[left_idx]  <= right[right_idx]:
			result.append(left[left_idx])
			left_idx += 1
		else:
			result.append(right[right_idx])
			right_idx += 1
	return(result)

	#add any reamiaing elements in the left or right lists
	if left_idx < len(left):
		result.extend(left[left_idx:])
	if right_idx < len(right):
		result.extend(right[right_idx:])

print(merge(a,b))

def merge_sort(m):
	if len(m) <=1:
		return(m)

	middle = len(m) // 2
	left = m[:middle]
	right = m[middle:]

	left = merge_sort(left)
	right = merge_sort(right)
	return(list(merge(left,right)))



'''
quick sort algorithm
'''

def quickSort(arr):
	less = []
	pivotList = []
	more = []
	arr_length = len(arr)
	if arr_length <= 1:
		return(arr)

	else:
		pivot = arr[0] ###of  chose pivot point
		#traverse the array
		for i in arr:
			if i < pivot:
				less.append(i)
			elif i > pivot:
				more.append(i)
			else:
				pivotList.append(i)
		#recurse on both sides
		less = quickSort(less)
		more = quickSort(more)
		return(less + pivotList + more)