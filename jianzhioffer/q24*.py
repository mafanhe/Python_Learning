# coding=utf-8


# 二叉搜索树的后序遍历序列
def verify_squence_of_BST(sequence):
	if not sequence:
		return False
	length = len(sequence)
	root = sequence[-1]
	i = 0
	while sequence[i]<root and i<length:
		i += 1
	j = i
	while sequence[j]>root and j<length:
		j += 1
	if j<length-1:
		return False
	left = right = True
	if i>1:
		left = verify_squence_of_BST(sequence[:i])
	if j-i>1:
		right = verify_squence_of_BST((sequence[i:j]))
	return left and right


# 二叉搜索树的前序遍历序列
def verify_sequence_of_BST2(sequence):
	if not sequence:
		return False
	length = len(sequence)
	root = sequence[0]
	i = 1
	while sequence[i]<root and i<length:
		i+=1
	j = i
	while sequence[j]>root and j<length:
		j+=1
	if j<length:
		return False
	left = right = True
	if i>2:
		left = verify_sequence_of_BST2(sequence[1:i])
	if j-i>1:
		right = verify_sequence_of_BST2((sequence[i:]))
	return left and right

if __name__ == "__main__":
	s1 = [5, 7, 6, 9, 11, 10, 8]
	s2 = [7, 4, 6, 5]
	s3= []
	print verify_squence_of_BST(s1)
	print verify_squence_of_BST(s2)
	print verify_squence_of_BST(s3)

