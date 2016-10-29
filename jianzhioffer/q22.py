# coding=utf-8


def is_pop_order(pPush, pPop):
	stack = [-1]
	i = 0
	j = 0
	while j < len(pPop):
		tmp = stack.pop()
		if i <= len(pPop):
			if tmp != pPop[j]:
				if i == len(pPop):
					return False
				stack.append(tmp)
				stack.append(pPush[i])
				i += 1
			else:
				j += 1
		elif j < len(pPop):
			return False
	return True

# 剑指offer answer
def is_pop_order2(pPush, pPop):
	bPossible = False
	lenth = len(pPop)
	if pPush and pPop:
		stack = [-1]
		i = 0
		j = 0
		while j < lenth:
			while not stack or stack[-1] != pPop[j]:
				if i == len(pPush):
					break
				stack.append(pPush[i])
				i += 1
			if stack[-1] != pPop[j]:
				break
			stack.pop()
			j += 1
		if len(stack)==1 and j == lenth:
			bPossible = True
	return bPossible

push = [1, 2, 3, 4, 5]
pop1 = [4, 5, 3, 2, 1]
pop2 = [1, 2, 5, 3, 4]
print is_pop_order2(push,pop1)