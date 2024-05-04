def  twosum(nums,target):
	'''
	这个函数只能解决两个数字和，且答案有且仅有一个的情况
	'''
	dict = {}
	for i in range(len(nums)):
		m = nums[i]
		if target - m in dict:#判定target - m 是否在字典中
			return (dict[target-m]+1,i +1) #存在返回连个数的下标
		dict[m] = i #若不存在则记录键值对的值
s =twosum([3,4,5,7,10],11)
print('下标是：',s)
