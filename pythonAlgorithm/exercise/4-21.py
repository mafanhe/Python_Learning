# coding=utf8

# find intervals that fall inside other intervals.


# 循环版本
def foo(intervals):
	intervals.sort(key=lambda a: a[0])		# 按左边坐标排序
	maxr = intervals[0][1]
	res = []
	for i in range(1,len(intervals)):
		if intervals[i][1] <= maxr:			# 如果右边坐标小于之前的最大右坐标，则在其他坐标内
			res.append(intervals[i])
		else:
			maxr = intervals[i][1]
	return res


# 递归版本
def foo2(intervals):
	intervals.sort(key=lambda a: a[0])
	res = []
	_foo2(intervals, res)
	return res


def _foo2(intervals,res):
	if len(intervals) == 1:
		return intervals[0][1]
	maxr = _foo2(intervals[:len(intervals)-1], res)
	if intervals[-1][1] <= maxr:
		res.append(intervals[-1])
	else:
		maxr = intervals[-1][1]
	return maxr

if __name__ == "__main__":
	intervals = [(0,4),(2,6),(3,4),(1,2)]
	intervals = [(0,4),(1,3),(2,3),(3,4)]
	print foo(intervals)
	print foo2(intervals)