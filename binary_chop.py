#encoding=utf-8

def binary_chop(list,v):
	low = 0 
	high = len(list)-1

	while low <= high:
		mid = (low+high)/2
		if v ==list[mid]:
			return mid
		if v > list[mid]:
			low = mid + 1
		else:
			high = mid - 1
	return None 


print binary_chop([1,2,3,4],5)

