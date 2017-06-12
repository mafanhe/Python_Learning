# coding=utf8
# merge and sort


def skyline(buildings):
	length = len(buildings)
	if length < 1:
		return buildings
	elif length == 1:
		# 一个矩形转换成两个天际线点——左上角和右下角
		return [[buildings[0][0],buildings[0][2]],[buildings[0][1],0]]
	# split to lft, rgt
	mid = length/2
	lft = skyline(buildings[0:mid])
	rgt = skyline(buildings[mid:])
	return merge(lft, rgt)


def merge(lft, rgt):
	i, j = 0, 0
	h1, h2 = None, None
	result = []
	while i < len(lft) and j < len(rgt):
		# merge的三种情况
		if lft[i][0] < rgt[j][0]:
			h1 = lft[i][1]
			new = [lft[i][0],max(h1,h2)]
			if result == [] or result[-1][1] != new[1]:
				result.append(new)
			i += 1
		elif lft[i][0] > rgt[j][0]:
			h2 = rgt[j][1]
			new = [rgt[j][0], max(h1,h2)]
			if result == [] or result[-1][1] != new[1]:
				result.append(new)
			j += 1
		else:
			h1 = lft[i][1]
			h2 = rgt[j][1]
			new = [lft[i][0], max(h1,h2)]
			if result == [] or result[-1][1] != new[1]:
				result.append(new)
			i += 1
			j += 1
	# 把剩余的点拼接进来
	while i < len(lft):
		if result == [] or result[-1][1] != lft[1]:
			result.append(lft[i][:])
		i += 1
	while j < len(rgt):
		if result == [] or result[-1][1] != rgt[1]:
			result.append(rgt[j][:])
		j += 1
	return result

if __name__ == "__main__":
	# sorted
	skylines = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
	print skylines
	print skyline(skylines)