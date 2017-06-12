n = int(raw_input())
A = [int(_) for _ in raw_input().split()]
# for i in range(n):
# 	A.append(int(raw_input()))
max = 0
cur = 0
lenth = 1
isUp= True
left = right = 0
maxlr=[]
for i in range(n):


	if A[i]>cur and isUp:
		right = i
		cur = A[i]
		lenth += 1
	elif A[i]<cur and not isUp:
		right = i
		cur = A[i]
		lenth += 1
	elif A[i]<cur and isUp and lenth>0:
		isUp = False
		right = i
		cur = A[i]
		lenth += 1
	elif (A[i]<cur and not isUp) or (A[i]>cur and not isUp) or (A[i]<cur and isUp and lenth==0):
		lenth = 2
		isUp = True
		left = right = i-1
	if lenth > max and not isUp:
		max = lenth
		maxlr = [left,right]
if n<3 or max<3:
	print -1,-1
else:
	print maxlr[0],maxlr[1]
