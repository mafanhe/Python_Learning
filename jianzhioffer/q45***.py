# coding:utf-8
# 面试题45：圆圈中最后剩下的数字（约瑟夫环）


#  用链表（数组也可以）来模拟环,时间效率O(mn), 空间效率O(n)
def last_remaining(l, m):
	pass


# 创新解法(递推公式，数学的魅力，时间效率O(n), 空间效率O(1) )
def last_remaining2(n, m):
	if n < 1 and m < 1:
		return -1
	last = 0
	for i in range(2, n+1):
		last = (last+m) % i
	return last

if __name__ == "__main__":
	print last_remaining2(6, 2)

