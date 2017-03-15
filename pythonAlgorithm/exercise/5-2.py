# fleury algorithm


# dfs
def dfs(x, map, ans=[]):
	ans.append(x)
	for i in range(len(map)):
		if map[x][i] >= 1:
			map[x][i] -= 1
			map[i][x] -= 1
			dfs(i, map, ans)
			break


# fleury
def fleury(x, map, ans=[]):
	ans.append(x)
	while ans:
		k = 0
		for i in range(len(map)):
			if map[ans[-1]][i] >= 1:
				k = 1
				break
		if k == 0:
			print(ans.pop())
		else:
			ans.pop()
			dfs(x, map, ans)


if __name__ == "__main__":
	map = [
		[0,1,0,0,1],
		[1,0,1,1,1],
		[0,1,0,1,0],
		[0,1,1,0,0],
		[1,1,0,0,0]
	]
	fleury(0,map,[])
