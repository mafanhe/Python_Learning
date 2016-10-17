def func(matrix):
	n = len(matrix)
	for i in range(n):
		x = 0
		y = i
		while y>=0:
			print matrix[x][y]
			x+=1
			y-=1

	for j in range(1,n):
		x = j
		y = n-1
		while x<n:
			print matrix[x][y]
			x+=1
			y-=1

matrix = [[1,2,3],[4,5,6],[7,8,9]]
func(matrix)
