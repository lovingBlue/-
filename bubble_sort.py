#encoding=utf-8

def bubble_sort(list):

	for i in range(len(list)):

		for j in range(i+1,len(list))[::-1]:
			if list[j]<list[j-1]:
				list[j],list[j-1]=list[j-1],list[j]
	return list


print bubble_sort([6,5,4,3])

'''
分析算法：
第5步 需要代价为c1 次数为n
第7步 需要代价为c2 次数为n(n-1)/2-1
第8步 需要代价为c3 次数为n(n-1)/2-1
第9步 需要代价为c4 次数为n(n-1)/2-1
此算法总运行时间为 c1*n + c2*(n*(n-1)/2-1) + c3*(n*(n-1)/2-1) + c4*(n*(n-1)/2-1)= O(n*n)
'''