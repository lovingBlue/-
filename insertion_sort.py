#encoding=utf-8


def insertion_sort(list):
	for j in range(1,len(list)):
		key = list[j]
		# insert list[j] into the sorted sequence list[1..j-1]  
		i = j-1
		while i>=0 and list[i]>key:
			list[i+1] = list[i]
			i = i-1
		list[i+1]=key
	return list

print insertion_sort([2,3,6,8])

'''
分析算法：
1.假设RAM模型，在RAM模型中，指令一条接一条执行，没有并发操作
2.RAM模型包含真实计算机常见的指令：算术指令、数据移动指令（装入、存储、复制）和控制指令。
  每条指令所需时间为常量
3.我们对每个数据字的规模假定一个范围。例如，当处理规模为n的输入时，整数有c*n位表示（c>=1）
4.假定RAM模型中，当k是一个足够小的正整数时，我们将把2^k的计算看成一个常量时间的操作
5.在RAM模型中，不考虑高速缓存和虚拟内存
'''