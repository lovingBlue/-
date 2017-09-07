#encoding=utf-8
def select_sort(list):
	length = len(list)
	for j in range(0,length):
		min =list[j]
		k=j
		#找到剩下数中最小的数与第j个进行交换
		for i in range(j+1,length):
			if list[i] < min:
				min = list[i]
				k=i			 
		list[k],list[j] = list[j],min
		

	return list
	
	

print select_sort([2,16,7,0,-1])